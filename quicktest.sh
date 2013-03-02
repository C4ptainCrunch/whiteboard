#!/bin/sh
set -v
rm -f db.sql sql.log && ./manage.py syncdb --noinput && ./manage.py populate && ./manage.py runserver
