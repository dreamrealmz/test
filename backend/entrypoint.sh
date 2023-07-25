#!/bin/bash

# Выполняем миграции Django
python manage.py migrate

# Собираем статические файлы Django
python manage.py collectstatic --noinput

# Запускаем сервер Django
python manage.py runserver 0:8000
