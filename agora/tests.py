"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from agora.models import Thread, CannotHaveChildren

T = Thread.objects.create

class SimpleTest(TestCase):
    def try_attach_node_to_thread(self):
        t = T(name="Thread Parent")
        t.attach(T(name="Thread enfant"))
    
    def test_attach(self):
        self.assertRaises(CannotHaveChildren, self.try_attach_node_to_thread)
