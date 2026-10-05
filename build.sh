#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate
python manage.py shell -c "from core.models import CompanyProfile; x=CompanyProfile.objects.get(pk=1); x.logo='company/APT_Grow_Together_Circular_Logo.png'; x.save(update_fields=['logo']); print('FIXED:', x.logo.name)"
python manage.py reset_admin