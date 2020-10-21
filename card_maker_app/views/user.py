import uuid
import os
from datetime import timedelta
from itertools import chain
from smtplib import SMTPException

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.utils.timezone import now
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from card_maker_app.models import User, PasswordResetToken, Card, CardLike
from card_maker_app.permissions import IsAdminDelete, IsAdminOrUpdateSelf, IsAuthenticatedFollow
from card_maker_app.serializers import UserSerializer, UserCreateSerializer, EmailSerializer, ResetPasswordSerializer, \
    UpdateEmailSerializer, CardOverviewSerializer, CardLikeSerializer, UserBanSerializer
from card_maker_app.utils.report import create_report


def item_date(instance):
    if 'card' in instance:
        return instance['card']['public']
    else:
        return instance['like']['created_at']


@permission_classes((IsAdminOrUpdateSelf, IsAdminDelete, IsAuthenticatedFollow))
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.data['password'])
        user.save()

        return Response(UserSerializer(user, context={'request': request}).data, status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def request_reset_password(self, request):
        password_reset = EmailSerializer(data=request.data)
        password_reset.is_valid(raise_exception=True)

        data = password_reset.data

        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            return Response(
                {'detail': 'A new mail has been sent to your mailbox at: ' + data['email']},
                status.HTTP_200_OK
            )

        try:
            PasswordResetToken.objects.get(user=user).delete()
        except PasswordResetToken.DoesNotExist:
            pass

        token = PasswordResetToken.objects.create(token=str(uuid.uuid4()), user=user)

        message = f'Go to {os.getenv("FRONTEND_URL")}/reset_password?token={token}" to reset your password'
        template = get_template('../../card_maker_app/templates/email.html')

        try:
            send_mail(
                subject='Password reset',
                message=message,
                html_message=template.render(
                    {
                        'url': f'{os.getenv("FRONTEND_URL")}/reset_password?token={token}',
                        'contact': f'{os.getenv("FRONTEND_URL")}/contact',
                        'home': os.getenv("FRONTEND_URL")
                    }),
                from_email='no-reply@cardmaker.com',
                recipient_list=[data['email']],
            )
        except BadHeaderError:
            raise ParseError('Invalid header found')
        except SMTPException:
            raise ParseError('There was an error sending the email')

        return Response(
            {'detail': 'A new mail has been sent to your mailbox at: ' + data['email']},
            status.HTTP_200_OK
        )

    @action(detail=False, methods=['post'])
    def reset_password(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        token = get_object_or_404(PasswordResetToken, token=data['token'])

        if token.created_at > now() + timedelta(hours=2):
            return Response({'detail': 'The token has expired'}, status=status.HTTP_400_BAD_REQUEST)

        token.user.set_password(data['password'])
        token.user.save()
        token.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def user_by_token(self, request):
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'}, status.HTTP_401_UNAUTHORIZED)

        return Response(UserSerializer(request.user, context={'request': request}).data, status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def update_email(self, request, pk):
        user = self.get_object()

        serializer = UpdateEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        if not user.check_password(data['password']):
            return Response({'detail': 'Password is incorrect'}, status.HTTP_400_BAD_REQUEST)

        user.email = data['email']
        user.save()

        return Response("", status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def follow(self, request, pk):
        user = request.user
        user_follow = self.get_object()

        if user_follow is user:
            return Response({'detail': 'Following yourself is not possible'}, status.HTTP_400_BAD_REQUEST)

        if user_follow in user.following.all():
            user.following.remove(user_follow)
        else:
            user.following.add(user_follow)

        return Response("", status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def timeline(self, request):
        user = request.user
        following = user.following.all()

        cards = map(lambda instance: {'card': instance}, CardOverviewSerializer(
            Card.objects.filter(public__isnull=False, user__in=following).order_by('-public'),
            many=True,
            context={'request': request}
        ).data)
        likes = map(lambda instance: {'like': instance}, CardLikeSerializer(
            CardLike.objects.filter(user__in=following),
            many=True,
            context={'request': request}
        ).data)

        timeline = sorted(
            chain(cards, likes),
            key=lambda instance: item_date(instance),
            reverse=True
        )

        return Response(timeline)

    @action(detail=True, methods=['post'])
    def report(self, request, pk):
        user = request.user
        parent = self.get_object()
        data = request.data
        data['user'] = user.pk

        return create_report(parent, data)

    @action(detail=True, methods=['post'])
    def ban(self, request, pk):
        user = self.get_object()

        if user.is_superuser:
            return Response({'detail': 'Admin user can not be banned'}, status.HTTP_400_BAD_REQUEST)

        data = request.data
        data['user'] = user.pk
        data['admin'] = request.user.pk

        serializer = UserBanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_ban = serializer.save()

        message = f'Your account has been restricted for violating our {user_ban.reason.name} policy if you believe' \
                  f' this is an error please appeal using the following link: {os.getenv("FRONTEND_URL")}/appeal/'
        template = get_template('../../card_maker_app/templates/restriction.html')
        try:
            send_mail(
                subject='Password reset',
                message=message,
                html_message=template.render(
                    {
                        'url': f'{os.getenv("FRONTEND_URL")}/appeal',
                        'contact': f'{os.getenv("FRONTEND_URL")}/contact',
                        'home': os.getenv("FRONTEND_URL"),
                        'reason': user_ban.reason.name.lower()
                    }),
                from_email='no-reply@cardmaker.com',
                recipient_list=[user.email],
            )
        except BadHeaderError:
            raise ParseError('Invalid header found')
        except SMTPException:
            raise ParseError('There was an error sending the email')

        return Response('', status.HTTP_204_NO_CONTENT)
