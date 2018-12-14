from rest_framework import routers, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """..."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        """..."""
        return self.request.user

