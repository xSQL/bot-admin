#!/bin/sh

# MANAGER OF SUPERVISOR

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

# Load settings.
LOCAL_SETTINGS="$BASE_DIR/world/etc/local_settings.sh"

# Import config file.
settings_is_loaded="false"
if [ -e $LOCAL_SETTINGS ]; then
    . $LOCAL_SETTINGS
    settings_is_loaded="true"
fi # end if ($LOCAL_SETTINGS).

# Information about import the configuration file.
if [ $settings_is_loaded = "false" ]; then
    # File does not exist!
    echo ""
    echo "Warning!"
    echo "You do not create a configuration file!"
    echo ""
    echo "Please, copy the template for configurations in \`etc\`" \
        "directory and adjust the settings: "
    echo "=> cp $BASE_DIR/world/usr/options/local_settings.sh.ex" \
        "$LOCAL_SETTINGS"
    echo ""

    exit 1
else
    # All ok.
    echo "Settings successfully loaded..."
fi # end if ().

# Show help.
if [ "$1" = "--start" ]; then
    sudo supervisorctl start $PROJECT_NAME
elif [ "$1" = "--stop" ]; then
    sudo supervisorctl stop $PROJECT_NAME
elif [ "$1" = "--status" ]; then
    sudo supervisorctl status $PROJECT_NAME
fi # end if (help).

exit 0

