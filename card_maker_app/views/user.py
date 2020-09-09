import uuid
import os
from datetime import timedelta
from smtplib import SMTPException

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.utils.timezone import now
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from card_maker_app.models import User, PasswordResetToken
from card_maker_app.permissions import IsAdminDelete, IsAdminOrUpdateSelf
from card_maker_app.serializers import UserSerializer, UserCreateSerializer, EmailSerializer, ResetPasswordSerializer


@permission_classes((IsAdminOrUpdateSelf, IsAdminDelete))
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
                status=status.HTTP_200_OK
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
            status=status.HTTP_200_OK
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
