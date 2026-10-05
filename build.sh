#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

echo "===== EXACT MEDIA TEST ====="

echo "Current directory:"
pwd

echo "MEDIA directory:"
ls -la media || true

echo "Checking exact 071 file:"
if [ -f "media/products/2026/10/071_abc_dry_powder_fire_extinguisher_2kg.png" ]; then
    echo "===== 071 FILE EXISTS ====="
    ls -lh "media/products/2026/10/071_abc_dry_powder_fire_extinguisher_2kg.png"
else
    echo "===== 071 FILE DOES NOT EXIST ====="
fi

echo "Searching for files containing 071:"
find media -type f -iname "*071*" -print || true

echo "Checking Django media settings:"
python manage.py shell -c "from django.conf import settings; print('MEDIA_URL =', settings.MEDIA_URL); print('MEDIA_ROOT =', settings.MEDIA_ROOT)"

echo "===== END EXACT MEDIA TEST ====="

python manage.py collectstatic --no-input

python manage.py migrate
python manage.py reset_admin