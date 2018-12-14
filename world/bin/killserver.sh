#!/bin/sh

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

# Kill server of project.
if [ -e "$BASE_DIR/world/var/run/gunicorn.pid" ]; then
    for pid in `cat "$BASE_DIR/world/var/run/gunicorn.pid"`
    do
        echo "Killed: $pid"
        kill -TERM $pid

        # kill -KILL $pid
        # kill -s KILL $pid
    done # end for ().
fi # end if ().

exit 0
