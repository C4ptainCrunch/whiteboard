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


    def to_dict(self):
        """Return self as a dict. Should be overridden in subclasses !"""
        res = self.short_dict()
        res['children'] = []
        for child in self.children():
            res['children'].append(child.short_dict())
        return res


    def short_dict(self):
        """Return self as a short dict with just identity informations"""
        return {'id':self.pk, 'name':str(self.name), 'type':self.classBasename()}


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
    lastmodif = models.DateTimeField(auto_now=True)
    
    def to_dict(self):
        res = Node.to_dict(self)
        res['description'] = self.description
        res['lastmodif'] = str(self.lastmodif)
        return res
    
    def save(self, *args, **kwargs):
        self.lastmodif = datetime.today()
        Node.save(self, *args, **kwargs)
    


class Course(Category):
    """Leaf container"""
    teacher = models.EmailField()
    mnemonic = models.CharField(max_length=10)

    def to_dict(self):
        res = Category.to_dict(self)
        res['teacher'] = self.teacher
        res['mnemomnic'] = self.mnemonic
        return res



class Taggable(Node):
    """An abstract taggable node. Taggable nodes have keywords."""
    keywords = models.ManyToManyField(Keyword)

    def to_dict(self):
        res = Node.to_dict(self)
        res['keywords'] = []
        for kw in self.keywords.all():
            res['keywords'].append(kw.to_dict())
        return res

