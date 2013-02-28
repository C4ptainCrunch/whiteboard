from django.db import models
from polymorphic import PolymorphicModel
from datetime import datetime
from keywords.models import Keyword

class Node(PolymorphicModel):
    """Base class for all P402 objects"""
    name = models.CharField(max_length=160)
    children = models.ManyToManyField("self", symmetrical=False)


class Category(Node):
    """Node container"""
    description = models.TextField()
    lastmodif = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        self.lastmodif = datetime.today()
        Node.save(self, *args, **kwargs)
    


class Course(Category):
    """Leaf container"""
    teacher = models.EmailField()
    mnemonic = models.CharField(max_length=10)


class Thread(Node):
    """Discussion"""
    keywords = models.ManyToManyField(Keyword)