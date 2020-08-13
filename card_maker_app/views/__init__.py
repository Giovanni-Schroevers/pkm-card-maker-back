from rest_framework.decorators import api_view
from rest_framework.response import Response
from .user import UserViewSet


@api_view(['GET'])
def index(request):
    return Response({"detail": "api works"})
