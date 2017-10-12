#!/bin/sh
python manage.py makemigrations
python manage.py sqlmigrate bitboard 0001
python manage.py migrate
echo "from django.contrib.auth.models import User;\
      User.objects.filter(email='admin@example.com').delete();\
      User.objects.create_superuser('admin', 'bitboard@gmail.com', 'fall2017')"\
      | python manage.py shell
exec "$@"
