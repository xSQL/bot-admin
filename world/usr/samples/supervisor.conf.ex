; Place this file in the `/etc/supervisor/conf.d/` directory and update
; supervisorctl configurations `sudo supervisorctl update`.

[program:<PROJECT_NAME>]
user = <USER>
stopsignal = TERM
autostart = true
autorestart = true
directory = <BASE_DIR>/world/etc/init.d/
command = <BASE_DIR>/world/etc/init.d/runserver.sh
stderr_logfile = <BASE_DIR>/world/var/log/supervisor_stderr.log
stdout_logfile = <BASE_DIR>/world/var/log/supervisor_stdout.log
