#!/bin/sh
set -v
rm -f db.sql sql.log && \
./manage.py syncdb --noinput && \
./manage.py populate  && \
./manage.py graphviz | dot -Tsvg > graph/static/graph.svg && \
#./manage.py compilehaml && \
./manage.py runserver
