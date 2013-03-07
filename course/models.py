from django.db import models
from graph.models import Category

# Create your models here.
class Course(Category):
    teacher = models.EmailField()
    mnemonic = models.CharField(max_length=10)
