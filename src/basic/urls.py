from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.contrib.auth import urls as accounts

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from .views import IndexView

urlpatterns = [
    url(r'^jwt/obtain/', obtain_jwt_token),
    url(r'^jwt/verify/', verify_jwt_token),

    url(r'^api/', include(('rest_framework.urls', 'rest_framework'))),
    url(r'^accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'^community/', include(('community.urls', 'community'), namespace='community')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
