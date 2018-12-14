import os, argparse
from subprocess import call

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    """
    Django wrapper form angular-cli commands
    """

    app_dirname = 'ng-source'

    def add_arguments(self, parser):
        """
        Add custom commands to bind angularng-cli
        """

        parser.add_argument('params', nargs='+')

    def ng_call(self, cmdlist, workpath):
        """
        Execute ng-cli command in source directory
        """

        cwd = os.getcwd()
        os.chdir(workpath)
        call(['ng']+cmdlist)
        os.chdir(cwd)

    def handle(self, *args, **options):
        """
        Set source directory of angular project and call ng-cli
        """

        params = options.get('params')
        label = params[0]

        ng_src_path = settings.NG_SRC_PATH
        if not ng_src_path:
            ng_src_path = settings.BASE_DIR
 
        if label=='init':
            self.ng_call(['new', self.app_dirname], ng_src_path)
        else:
            workpath = os.path.join(ng_src_path, self.app_dirname)
            self.ng_call(params, workpath)
