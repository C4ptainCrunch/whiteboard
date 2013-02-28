"""
fill.py - 28/02/2013

Fills the DB with lots of data
"""

from poly.models import *
from random import randint

for i in xrange(1000):
    Category.objects.create(name=str(randint(0,1000)),description=str(randint(0,1000)))
    Thread.objects.create(subject=str(randint(0,1000)),caca=str(randint(0,1000)))
    Course.objects.create(name=str(randint(0,1000)),mnemo='INFO-F-'+str(randint(0,599)),prof=str(randint(0,1000)))
    Document.objects.create(name=str(randint(0,1000)),original=str(randint(0,1000)),flags=(randint(0,1000)))