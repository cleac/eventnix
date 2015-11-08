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
        IS_VENV=${VIRTUAL_ENV}
        if [[ ! -n ${IS_VENV} ]]; then
            source .venv/bin/activate
        else
            echo -e "already in virtualenv: $IS_VENV"
        fi
        cd src
        # Listening to localhost. Use nginx proxying in case of production
        gunicorn eventnix:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornWebWorker
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
