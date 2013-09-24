#!/bin/sh

DOWNLOAD_DIR=./src

# test for git and hg commands
for cmd in git hg; do
    command -v ${cmd} >/dev/null || { echo "sh: command not found: ${cmd}"; exit 1; }
done

# download all packages to ./src (default)
pip install --no-install -r requirements.txt

cp -r ${DOWNLOAD_DIR}/django-autoload/autoload ./autoload
cp -r ${DOWNLOAD_DIR}/django-dbindexer/dbindexer ./dbindexer
cp -r ${DOWNLOAD_DIR}/django-nonrel/django ./django
cp -r ${DOWNLOAD_DIR}/djangoappengine/djangoappengine ./djangoappengine
cp -r ${DOWNLOAD_DIR}/djangotoolbox/djangotoolbox ./djangotoolbox

[ -f ${DOWNLOAD_DIR}/pip-delete-this-directory.txt ] && rm -rf ${DOWNLOAD_DIR}

echo "Now run:
./manage.py runserver

To launch this app. If you want access to django /admin, run also:
./manage.py createsuperuser

And then login in <your_app_ip>/admin, probably http://127.0.0.1:8000/admin"


