set -o errexit
set -o nounset

echo "Run manage.py migrations"
#python /usr/app/manage.py collectstatic --noinput
#python /usr/app/manage.py makemigrations --noinput
#python /usr/app/manage.py migrate --noinput

echo "Run server"
#exec python -Wd /usr/app/manage.py runserver 0.0.0.0:8000
#exec gunicorn /usr/app/shop/wsgi:application -b 0.0.0.0:8000 --reload

