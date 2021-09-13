#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

# Esto es para desarrollo
python /app/manage.py migrate
python /app/manage.py runserver 0.0.0.0:8000

