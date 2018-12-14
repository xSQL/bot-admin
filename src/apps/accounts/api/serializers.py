from rest_framework import routers, serializers, viewsets, generics

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """..."""
    class Meta:
        model = User
        fields = (
            'first_name', 'middle_name', 'last_name', 'skype', 'phone', 
            'telegram'
        )

