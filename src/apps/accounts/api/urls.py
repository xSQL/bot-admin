from django.conf.urls import url

from rest_framework import routers

from .views import LoginView
from .viewsets import UserViewSet

v = lambda x: x.as_view()

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^login/$', v(LoginView))
]
