from django.db import models
from polymorphic import PolymorphicModel
from datetime import datetime
from keywords.models import Keyword

class Node(PolymorphicModel):
    """Base class for all P402 objects"""
    name = models.CharField(max_length=160)
    _children = models.ManyToManyField("self", symmetrical=False)
    
    def classBasename(self):
        """Return the class name without modules prefix"""
        klass = str(type(self)) # "<class 'foo'>"
        j = len(klass)-2
        i = j
        while i>0 and klass[i-1]!='.':
            i -= 1
        return klass[i:j]
    
    
    def __repr__(self):
        return '<%s:%d "%s">'%(self.classBasename(), self.pk, self.name)
    
    
    def children(self):
        """Return a list of all self's children"""
        return self._children.all()
    
    
    def ancestors(self):
        """Return a list of all self's ancestors"""
        return Node.objects.filter(_children=self)
    
    
    def hasCycle(self, traversed):
        """Recursively walk the graph to find any loop"""
        res = False
        if self in traversed:
            res = True
        else:
            traversed.append(self)
            for child in self.children():
                if child.hasCycle(traversed):
                    res = True
                    break
            traversed.pop()
        return res
    
    
    def attach(self, child, acyclic_check=True):
        """
        Attach a new child to self and return True. If acyclic_check evaluates
        to True, and a loop occurs with this new edge, don't add the new child
        and return False.
        """
        res = True
        if acyclic_check and child.hasCycle([self]):
            res = False
        else:
            self._children.add(child)
            self.save()
        return res
    


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
