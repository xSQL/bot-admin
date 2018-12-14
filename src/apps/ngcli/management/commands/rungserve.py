import os, signal, time
from sys import stdout, stdin, stderr
from subprocess import Popen, call

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """RUnserver && NG Serve combine"""

    commands = [
       'python src/manage.py runserver',
       'python src/manage.py ng serve',
    ]


    def handle(self, *args, **options):
        """
        Execute all commands from commandlist
        """
        proclist = list()
        for cmd in self.commands:
            proc = Popen(cmd, shell=True, stdin=stdin, stdout=stdout, 
                stderr=stderr
            )
            proclist.append(proc)
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            for proc in proclist:
                os.kill(proc.pid, signal.SIGKILL)


