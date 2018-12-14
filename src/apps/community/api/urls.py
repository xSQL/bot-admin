from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include


from .viewsets import ExtensionViewSet, CommunityView, CommunityListView, \
    SynonymListView, SynonymView

router = routers.DefaultRouter()

router.register(r'extensions', ExtensionViewSet)

urlpatterns = [
    url(r'^groups/$', CommunityListView.as_view()),
    url(r'^group/(?P<pk>\d+)/$', CommunityView.as_view()),
    url(r'^synonyms/$', SynonymListView.as_view()),
    url(r'^synonym/(?P<pk>\d+)/$', SynonymView.as_view()),
]
