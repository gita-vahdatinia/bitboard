#!/bin/sh
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User;\
      User.objects.filter(email='admin@example.com').delete();\
      User.objects.create_superuser('admin', 'admin@example.com', 'fall2017')"\
      | python manage.py shell

exec "$@"
