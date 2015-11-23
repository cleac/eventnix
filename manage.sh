#!/bin/bash

USER_DIRECTORY=`pwd`
SCRIPT_DIRECTORY=`dirname $(realpath $0)`

USAGE_STRING="manage.sh <command> [arguments]"
COMMANDS="\
    run \t\t run server
"

COMMAND=$1

if [[ ! -n ${COMMAND} ]]; then
    echo -e "Usage: $USAGE_STRING" >&2
    exit 1
fi

# All paths here are relative to SCRIPT_DIRECTORY
cd ${SCRIPT_DIRECTORY}

case ${COMMAND} in
    'run')
        CONFIG_FILE=$2
        if [[ ! -n ${CONFIG_FILE} ]]; then
            die "No config file specified"
        else
            CONFIG_FILE=`realpath ${CONFIG_FILE}`
        fi
        IS_VENV=${VIRTUAL_ENV}
        if [[ ! -n ${IS_VENV} ]]; then
            source .venv/bin/activate
        else
            echo -e "already in virtualenv: $IS_VENV"
        fi
        cd src
        # Edit gunicorn config file
        gunicorn 'eventnix:build_app(config_file="'${CONFIG_FILE}'")' -c ${SCRIPT_DIRECTORY}/config/gunicorn.py
        cd ../
        if [[ ! -n ${IS_VENV} ]]; then
            deactivate
        fi
    ;;
    *)
        echo -e "Invalid command \"${COMMAND}\"" >&2
        echo -e "Available commands: \n${COMMANDS}" >&2
        exit 1
    ;;
esac

# Return to where user was before calling this script
cd ${USER_DIRECTORY}
