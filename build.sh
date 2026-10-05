#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate
python manage.py shell -c "from django.apps import apps; print([(m._meta.label, f.name) for m in apps.get_models() for f in m._meta.fields if f.get_internal_type() in ('ImageField','FileField')])"
python manage.py reset_admin