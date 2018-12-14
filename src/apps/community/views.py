from django.views.generic import ListView

from .models import Extension


class ExtensionList(ListView):
    """..."""
    template_name = 'community/extension/list.jinja'
    model = Extension
