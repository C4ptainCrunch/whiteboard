"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from agora.models import Thread

T = Thread.objects.create

class SimpleTest(TestCase):
    def test_attach(self):
        t = T(name="Thread Parent")
        self.assertRaises(Thread.CannotHaveChildren, t.attach(T(name="Thread enfant")))
