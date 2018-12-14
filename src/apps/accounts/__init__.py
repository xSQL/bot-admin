from os import path

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

APP_NAME = 'accounts'
VERBOSE_APP_NAME = _('Users & Groups')

class AppVerboseNameConfig(AppConfig):
    name = APP_NAME
    verbose_name = VERBOSE_APP_NAME

default_app_config = '%s.__init__.AppVerboseNameConfig'%(APP_NAME,)
