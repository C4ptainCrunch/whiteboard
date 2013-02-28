from django.db import models
from polymorphic import PolymorphicModel

class Node(PolymorphicModel):
    pass

class Category(Node):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=99)

class Course(Node):
    name = models.CharField(max_length=100)
    mnemo = models.CharField(max_length=100)
    prof = models.CharField(max_length=50)

class Thread(Node):
    subject = models.CharField(max_length=100)
    caca = models.CharField(max_length=100)

class Document(Node):
    name = models.CharField(max_length=100)
    original = models.CharField(max_length=100)
    flags = models.IntegerField(max_length=100)