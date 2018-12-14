#!/bin/sh

#                                                                             #
# CLEAR TEMPORARY AND UNNECESSARY FILES IN PROJECT'S DIRECTORIES.             #
#                                                                             #

# A list of directories, relative to the root path, where will search for files.
# ** Specify the path from the root directory of the project.
DIRECTORY_LIST="./src ./world/etc"

# Files that are subject to removal.
FILE_LIST="*.pyc *.core"

# Set `DEBUG` as "true" for script testing.
DEBUG="false"

# Determine the root directory of the project.
# *** Root directory - the directory that contains: `src`, `venv`, `world` etc,
#     a 100% `src/manage.py` file exists.
BASE_DIR_FILE_MARKER="src/manage.py"
ABSOLUTE_FILENAME=`readlink -e "$0"`
BASE_DIR=`dirname "$ABSOLUTE_FILENAME"`
BASE_DIR_EXIST=0
while [ true ]
do
    if [ -e $BASE_DIR/$BASE_DIR_FILE_MARKER ]; then
        # Directory exist.
        BASE_DIR_EXIST=1
        echo "BASEDIR: $BASE_DIR"
        break
    fi # ...

    BASE_DIR=`dirname "$BASE_DIR"`
    if [ $BASE_DIR = "/" ]; then
        # The directory was not found - use the current directory.
        BASE_DIR=`dirname "$ABSOLUTE_FILENAME"`
    fi # ...
done # end while ().

if [ $BASE_DIR_EXIST != 1 ]; then
    echo "BASEDIR not exist!"
    exit 1
fi

# Go to the root directory.
cd $BASE_DIR

# Displai script info.
echo "Now will be removed: $FILE_LIST files in: $DIRECTORY_LIST directories."
echo "To stop the script, press Ctrl+C."
if [ "$DEBUG" = "true" ]; then
    echo "** Debugging is enabled: files will not be deleted."
fi # end if (DEBUG).
sleep 1

change="false"
scanning="true"
while true
do
    count=0

    for dir in $DIRECTORY_LIST
    do # See all directory.
        for filename in $FILE_LIST
        do # See all files.

            for file in `find $dir/ -name "$filename" -type f`
            do # Remove *.pyc in all folders.
                echo "Remove: $file"
                change="true"
                count=`expr $count + '1'`
                if [ "$DEBUG" = "false" ]; then
                    echo "File: $file"
                    rm -f $file
                fi
            done # end for FIND.

            for link in `find $dir/* -type l`
            do # Remove *.pyc in all symbol links folders.
                for file in `find $file/ -name "$name" -type f`
                do
                    echo "Remove: $file"
                    change="true"
                    if [ "$DEBUG" = "false" ]; then
                        rm -f $file
                    fi
                done # end for FIND.
            done # end for LINK.

        done # end for FILE_LIST.
    done # end for DIRECTORY_LIST.

    if [ "$change" = "true" ]; then
        echo "Remove finish."
        echo "Removed: $count"
        change="false"
        scanning="true"
    else
        if [ "$scanning" = "true" ]; then
            echo 'Scanning ... '
            scanning="false"
        fi
    fi # end if (change).

    sleep 2
done # end while.

exit 0
