from rest_framework.viewsets import ModelViewSet

from lib.models import User
from lib.serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
