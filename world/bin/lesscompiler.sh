#!/bin/sh

#                                                                             #
# LESS COMPILLER.                                                             #
#                                                                             #
# ** Install lesscpy package.                                                 #

# Ignore compilation if the file name (starting with the src/ directory) has
# one of the substring:
FILE_IGNORE_LIST="$*"

# Set `DEBUG` as "true" for script testing.
DEBUG="false"

# Must be installed lesscpy package.
echo "Check lesscpy package ..."
which lesscpy

if [ $? -ne 0 ]; then
    echo "Not installed lesscpy package."
    echo "  Install:"
    echo "  python-lesscpy - LessCss Compiler for Python 2.x"
    echo "  python3-lesscpy - LessCss Compiler for Python 3.x"
    exit 1
fi

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

if [ $BASE_DIR_EXIST -ne 1 ]; then
    echo "BASEDIR not exist!"
    exit 1
fi

# Go to the root directory.
cd $BASE_DIR

if [ "$DEBUG" = "true" ]; then
    echo "** Debugging is enabled: files will not be compiled."
    sleep 1
fi # end if (DEBUG).

echo "Started compiling..."

forced="true"
changed="true"
compile="true"
while true
do
    # View all files.
    for input_filename in `find . -type f -name *.less`
    do
        compile="true"
        output_filename="${input_filename%.*}.css"

        # The file should not be on the ignore list.
        for ignore in $FILE_IGNORE_LIST
        do
            has=`echo $input_filename $ignore | awk '{print index($1,$2)}'`
            if [ $has -ne 0 ]; then
                compile="false"
                break
            fi
        done

        # If the compilation is allowed.
        if [ $compile = "true" ]; then

            # If source has been changed.
            if [ $forced = "true" ]; then
                # Start forced compilation if it is the first run.
                seek_stat=30
            else
                # The difference time of modified files.
                input_stat=$(stat --print=%Y $input_filename)
                if [ $? -ne 0 ]; then
                    input_stat=0
                fi

                output_stat=$(stat --print=%Y $output_filename)
                if [ $? -ne 0 ]; then
                    output_stat=$(echo "$input_stat - 30" | bc)
                fi

                seek_stat=$(echo "$input_stat - $output_stat" | bc)
            fi # end source has been changed.

            # If dependence has been changed.
            # ** If source less file has import some depending, use import
            # (i.e. @import "some/file.less";), and this depending has been
            # changed.
            if [ $seek_stat -le 10 ]; then
                # If the imported file has been modified - forced to recompile
                # the current file.
                current_dir=`dirname "$input_filename"`
                _search_import=

                for import_filename in \
                    `grep -w "@import" $input_filename | \
                    sed 's/.*@import "\([^"]*\)";.*/\1/'`
                do
                    # File of import.
                    import_filename="${current_dir}/${import_filename}"

                    # The difference time of modified files.
                    output_stat=$(stat --print=%Y $output_filename)
                    if [ $? -ne 0 ]; then
                        output_stat=0
                    fi

                    import_stat=$(stat --print=%Y $import_filename)
                    if [ $? -ne 0 ]; then
                        import_stat=$(echo "$input_stat - 30" | bc)
                    fi

                    seek_stat=$(echo "$import_stat - $output_stat" | bc)
                    if [ $seek_stat -ge 10 ]; then
                        echo "Dependence has been changed: $import_filename"
                        break
                    fi
                done
            fi # end dependence has been changed.

            # Compile or show files.
            if [ "$DEBUG" = "false" ]; then
                if [ $seek_stat -ge 10 ]; then
                    changed="true"
                    lesscpy -V -s 4 $input_filename > $output_filename
                fi
            else
                echo $input_filename " => $output_filename"
            fi # end if DEBUG.

        fi # end if compile.
    done # end for find all less.

    if [ $changed = "true" ]; then
        echo ""
        echo "Waiting for change..."
        echo ""
    fi

    changed="false"
    forced="false"
    sleep 0.5
done # end while.

exit 0

