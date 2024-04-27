#!/bin/bash

set -e

python unilime/manage.py migrate  # Run the migration command
python unilime/manage.py collectstatic --noinput  # Collect static files
exec gunicorn unilime.wsgi:application --bind 0.0.0.0:9310
