from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.conf import settings as apps


class LoginRequiredMixin(object):
    """The mixin of the `login required` for class based views.

    Only authorized users can work with this views. And unauthorized users will
    be redirected to `settings.LOGIN_URL`, passing the current absolute path in
    the query string, for example: /accounts/login/?next=/profile/.

    Usage:
        class ProfileView(LoginRequiredMixin, TemplateView):
            template_name = 'profile.html'

    Settings:
        `ACCOUNTS_REDIRECT_FIELD_NAME` - the GET param name which indicates
            the redirect path after successful login (defaults: 'next', i.e:
            `django.contrib.auth.REDIRECT_FIELD_NAME`)

        `ACCOUNTS_LOGIN_URL` - the login url (default: /accounts/login/ i.e:
            `settings.LOGIN_URL`).

    """
    @method_decorator(
        login_required(
            login_url=apps.LOGIN_URL,
            redirect_field_name=apps.REDIRECT_FIELD_NAME
        )
    )
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



class StaffRequiredMixin(object):
    """..."""
    @method_decorator(
        login_required(
            login_url=apps.LOGIN_URL,
            redirect_field_name=apps.REDIRECT_FIELD_NAME
        )
    )
    def dispatch(self, request, *args, **kwargs):
        """..."""
        if not request.user.is_staff:
            raise Http404

        return super().dispatch(request, *args, **kwargs)
