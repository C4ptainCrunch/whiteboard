"""
get.py - 28/02/2013

Retrieves data from DB, and writes queries to stderr
"""


from poly.models import *
from random import randint

import logging
l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())


for i in Thread.objects.filter(subject=5):
    pass