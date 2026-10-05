#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate
python manage.py shell -c "from django.apps import apps; from django.db.models import Q; needle='mb823Sx'; [(print('FOUND:',m._meta.label,f.name,obj.pk,getattr(obj,f.name).name)) for m in apps.get_models() for f in m._meta.fields if f.get_internal_type() in ('ImageField','FileField') for obj in m.objects.all() if needle in str(getattr(obj,f.name,''))]"
python manage.py reset_admin