from django.conf.urls import url, include

from .api import urls as api_urls

urlpatterns = [
    url(r'^', include(api_urls.router.urls)),
    url(r'^', include(api_urls)),
    
]
