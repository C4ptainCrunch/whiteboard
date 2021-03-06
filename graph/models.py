from django.db import models
from polymorphic import PolymorphicModel
from datetime import datetime
from keywords.models import Keyword
import re

class CannotHaveChildren(Exception):
    """Exception raised by graph nodes that doesn't accept children"""
    def __init__(self, node):
        msg = node.classBasename()+'#'+str(node.pk)+' can\'t have children'
        Exception.__init__(self, msg)
    


class Node(PolymorphicModel):
    """Base class for all P402 objects"""
    name = models.CharField(max_length=160)
    _children = models.ManyToManyField("self", symmetrical=False)

    def classBasename(self):
        """Return the class name without modules prefix"""
        klass = str(type(self)) # "<class 'foo.bar'>"
        return re.sub(r'.*[\.\']([^\.]+)\'>$', r'\1', klass)

    
    @property
    def canonic_url(self):
        return '/'+self.classBasename().lower()+'/'+str(self.pk)


    def to_dict(self, with_children=False):
        res = {'id':self.pk, 'name':str(self.name), 'type':self.classBasename()}
        res['url'] = self.canonic_url
        if with_children:
            res['children'] = []
            for child in self.childrens():
                res['children'].append(child.to_dict(False))
        return res
    
    def __repr__(self):
        return '<%s:%d "%s">'%(self.classBasename(), self.pk, self.name)


    def childrens(self):
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
            for child in self.childrens():
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

    def detatch(self,parent):
        """
        Detatch self from parent. Return none
        """
        parent._children.remove(self)
        parent.save()

    def childrens_tree(self):
        """
        Returns a tree of the node's  childrens by depth-first search
        """
        tree = {}
        for node in self.children.all():
            tree[node] = f.descendants_tree()
        return tree

    def childrens_iterator(self):
        """
        Yields the node's childrens by depth-first search
        """
        # TODO : add some backtracking to prevent going twice in some places
        yield self
        for child in self.childrens():
            for node in child.childrens_iterator():
                yield node
                
    def is_child(self,other):
        """
        Retruns True if other is an acnestor of self. Otherwise False
        """
        return self in  other.childrens_iterator()

    def distance(self, target):
        return len(self.path(target))





class Category(Node):
    description = models.TextField()
    lastmodif = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.lastmodif = datetime.today()
        Node.save(self, *args, **kwargs)



class Taggable(Node):
    """An abstract taggable node. Taggable nodes have keywords."""
    keywords = models.ManyToManyField(Keyword)

    @staticmethod
    def KW(name):
        """Simply create or get a keyword"""
        #Keywords are always lowercased
        existing, created = Keyword.objects.get_or_create(name=name.lower())
        return existing if existing else created
    
    def add_keyword(self, *tags):
        """Add a keyword by directly passing its name"""
        for tag in tags:
            self.keywords.add(self.KW(tag))
    
    def related_list(self):
        """
        Return a list of taggable objects that share some keywords with self.
        """
        res = []
        for kw in self.keywords.all():
            for node in kw.taggable_set.all():
                if node in res:
                    res.remove(node)
                    res.insert(0, node)
                else:
                    res.append(node)
        return res
                    
    related = related_list
    