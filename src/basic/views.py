from django.views.generic import TemplateView
from django.utils import timezone as tz
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.views.generic import CreateView
from django.core.mail import EmailMessage

from accounts.permissions import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    """..."""
    template_name = 'index.jinja'


