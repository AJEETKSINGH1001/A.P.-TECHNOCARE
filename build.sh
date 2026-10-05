#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

echo "===== CHECK MEDIA ====="
pwd
ls -la
ls -la media || true
find media -type f | head -30 || true
echo "===== END MEDIA CHECK ====="

python manage.py collectstatic --no-input

python manage.py migrate
python manage.py reset_admin