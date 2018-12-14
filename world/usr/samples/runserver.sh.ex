#!/bin/sh

# Configurations.
HOST="127.0.0.1"
PORT="<PORT>"

# Determine the root directory of the project.
# *** Root directory - the directory that contains: `src`, `venv`, `world` etc,
#     a 100% `src/manage.py` file exists.
BASE_DIR_FILE_MARKER="src/manage.py"
ABSOLUTE_FILENAME=`readlink -e "$0"`
BASE_DIR=`dirname "$ABSOLUTE_FILENAME"`
while [ true ]
do
    if [ -e $BASE_DIR/$BASE_DIR_FILE_MARKER ]; then
        # Directory exist.
        break
    fi # ...

    BASE_DIR=`dirname "$BASE_DIR"`
    if [ $BASE_DIR = "/" ]; then
        # The directory was not found - use the current directory.
        BASE_DIR=`dirname "$ABSOLUTE_FILENAME"`
    fi # ...
done # end while ().

cd $BASE_DIR

# For CSH/TCSH
## source $BASE_DIR/venv/bin/activate.csh

# For BASH
## source $BASE_DIR/venv/bin/activate

# For SH
. $BASE_DIR/venv/bin/activate

cd $BASE_DIR/src
gunicorn -w 1 --bind ${HOST}:${PORT} \
    --pid="$BASE_DIR/world/var/run/gunicorn.pid" \
    --timeout=15 \
    --log-file="$BASE_DIR/world/var/log/gunicorn_stdout.log" \
    "basic.wsgi:application"

deactivate
exit 0

