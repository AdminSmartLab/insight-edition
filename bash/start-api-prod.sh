#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

/usr/local/bin/gunicorn config.wsgi --bind 0.0.0.0:8000 --chdir=/api