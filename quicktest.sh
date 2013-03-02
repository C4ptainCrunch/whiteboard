#!/bin/sh

set -v

rm -f db.sql && ./manage.py syncdb && ./manage.py populate && ./manage.py runserver