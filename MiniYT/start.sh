#!/usr/bin/env bash

chmod +x ./wait-for-it.sh 

./wait-for-it.sh db:5432 -- python manage.py makemigrations && python manage.py migrate && echo "SETTING SUPERUSER" && python manage.py initsuperuser --username root --password root --noinput --email 'admin@admin.com' && python manage.py runserver 0.0.0.0:8000