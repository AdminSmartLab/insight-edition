#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

python /api/manage.py runserver 0.0.0.0:8000

