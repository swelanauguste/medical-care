#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

python manage.py makemigrations
python manage.py migrate
# python manage.py flush --noinput
python manage.py createsuperuser --username kingship --email kingship.kc@gmail.com --noinput

# python manage.py add_qualifications
# python manage.py add_skills
# python manage.py add_skill_level
# python manage.py add_tags
# python manage.py add_locations
# python manage.py add_work


python manage.py collectstatic --noinput

exec "$@"