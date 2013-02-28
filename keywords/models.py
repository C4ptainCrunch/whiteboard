from django.db import models

class Keyword(models.Model):
    """
    Keywords are a comfortable way to group object that are far from each other 
    in the site's graph, but semantically close.
    """
    name = models.CharField(max_length=50)
