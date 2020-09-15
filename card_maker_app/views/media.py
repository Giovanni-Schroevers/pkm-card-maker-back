from django.db.models import Q
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from card_maker import settings
from card_maker_app.models import Card, User


@api_view(['GET'])
@permission_classes((AllowAny,))
def media_access(request, path):
    access_granted = has_permission(path, request.user)

    if access_granted:
        if settings.DEBUG:
            try:
                raw_file = open(settings.MEDIA_ROOT + '/' + str(path), 'rb')
            except Exception as e:
                return Response(e, status.HTTP_500_INTERNAL_SERVER_ERROR)

            return HttpResponse(raw_file.read(), content_type='image/')

        response = HttpResponse()
        del response['Content-Type']
        response['X-Accel-Redirect'] = '/protected/media/' + path
        return response
    else:
        return Response({'detail': 'Not authorized to access this media.'}, status.HTTP_401_UNAUTHORIZED)


def has_permission(path, user):
    if user.is_authenticated:
        if user.is_staff:
            return True

    if User.objects.filter(photo=path):
        return True

    if Card.objects.filter(
        Q(background_image=path) |
        Q(card_image=path) |
        Q(top_image=path) |
        Q(type_image=path) |
        Q(prevolve_image=path) |
        Q(custom_set_image=path)
    ):
        return False

    if Card.objects.filter(full_card_image=path):
        return True

    return False
