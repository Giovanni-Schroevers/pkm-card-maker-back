from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from card_maker_app.models import User
from card_maker_app.permissions import IsAdminDelete, IsAdminOrUpdateSelf
from card_maker_app.serializers import UserSerializer, UserCreateSerializer


@permission_classes((IsAdminOrUpdateSelf, IsAdminDelete))
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()

        return Response(UserSerializer(user).data, status.HTTP_201_CREATED)
