from rest_framework import routers, serializers, viewsets, generics

from ..models import Extension, Community, Synonym


class ExtensionSerializer(serializers.ModelSerializer):
    """..."""
    class Meta:
        model = Extension
        fields = ('name', 'description')


class CommunitySerializer(serializers.ModelSerializer):
    """..."""
    class Meta:
        model = Community
        fields = ('pk', 'name', 'community_id')


class SynonymListSerializer(serializers.ModelSerializer):
    """..."""
    community = serializers.ReadOnlyField(source='community.name')
    class Meta:
        model = Synonym
        fields = ('pk', 'name', 'text', 'community')


class SynonymItemSerializer(serializers.ModelSerializer):
    """..."""
    community = serializers.PrimaryKeyRelatedField(queryset=Community.objects.all())
    class Meta:
        model = Synonym
        fields = ('pk', 'name', 'text', 'community')
