from django.conf.urls import url, include
from django.contrib.auth import forms as auth_forms, views as auth_views
from django.views.generic.edit import CreateView, UpdateView, FormView

from .views import UpdateUser, SignUpView, FilePlupload, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView,\
    ConfirmView

from .api import urls as api_urls

v = lambda cls: cls.as_view()

urlpatterns = [
    url(r'^api/', include('accounts.api.urls')),
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'accounts/login.jinja'},
        name='login'
    ),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^reset-password/$', v(PasswordResetView), name='reset-password'),
    url(r'^reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        v(PasswordResetConfirmView),
        name='reset-confirm'),
    url(r'^reset-done/$', v(PasswordResetDoneView), name='reset-done'),
    url(r'^reset-complete/$',
        v(PasswordResetCompleteView),
        name='reset-complete'
    ),
    url(r'^confirm/(?P<token>[0-9A-Za-z]{32})/$',
        v(ConfirmView), 
        name='confirm'),
    url(r'^signup/', v(SignUpView), name='signup'),
    url(r'^update-user/', v(UpdateUser), name='update-user'),
    url(r'^plupload/$', v(FilePlupload), name='plupload'),
    url(r'^', include(api_urls.router.urls)),
    url(r'^', include(api_urls)),
 ]
