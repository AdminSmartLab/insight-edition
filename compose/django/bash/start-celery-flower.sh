#!/bin/sh

set -o errexit
set -o nounset


celery flower \
    --app=adminsmart.taskapp \
    --broker="${CELERY_BROKER_URL}" \
    --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"
