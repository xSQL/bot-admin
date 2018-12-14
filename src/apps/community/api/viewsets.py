from rest_framework import routers, viewsets, generics, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..models import Extension, Community, Synonym
from .serializers import ExtensionSerializer, CommunitySerializer,\
    SynonymItemSerializer, SynonymListSerializer


class ExtensionViewSet(viewsets.ModelViewSet):
    """..."""
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer


class CommunityListView(generics.ListCreateAPIView):
    """..."""
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def perform_create(self, serializer):
        """..."""
        serializer.validated_data['owner'] = self.request.user
        return super().perform_create(serializer)


class CommunityView(generics.RetrieveUpdateDestroyAPIView):
    """..."""
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class SynonymPagination(pagination.PageNumberPagination):
    """..."""
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


class SynonymListView(generics.ListCreateAPIView):
    """..."""
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Synonym.objects.all()
    serializer_class = SynonymListSerializer
    pagination_class = SynonymPagination
    
    def perform_create(self, serializer):
        """..."""
        community = Community.objects.get(
            owner=self.request.user,
            pk=self.request.data.get('community')
        )
        serializer.validated_data['community'] = community
        return super().perform_create(serializer)


class SynonymView(generics.RetrieveUpdateDestroyAPIView):
    """..."""
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Synonym.objects.all()
    serializer_class = SynonymItemSerializer

