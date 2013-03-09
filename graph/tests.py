"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from course.models import Course
from graph.models import Node, Category, Taggable

class SimpleTest(TestCase):
    def test_basename(self):
        """Playing with names"""
        n = Node.objects.create()
        pk = n.pk
        self.assertEqual('Node', n.classBasename(), 'Class basename')
        self.assertEqual('/node/'+str(pk), n.canonic_url(), 'Canonic URL')
    
    
    def test_graph(self):
        """Basic graph manipulation"""
        a, b, c = (Node.objects.create() for i in range(3))
        a.attach(b); b.attach(c) #A->B->C
        
        self.assertTrue(a.attach(c), 'A->B->C && A->C')
        
        self.assertIn(b, a.childrens(), 'Graph walk')
        self.assertIn(b, a.childrens_iterator(), 'Graph walk using iterator')
        self.assertIn(a, b.ancestors(), 'Reverse graph walk')
        self.assertFalse(c.attach(a), 'Cycle')
        self.assertTrue(c.attach(a, False), 'Force cyclic attach')
        self.assertFalse(a.attach(b), 'Attach existing child')
        self.assertTrue(b.is_child(a), 'Genetics check')
        self.assertEqual(1, a.distance(b), 'Distance between nodes')
    
    
    def test_tags(self):
        a, b, c = (Taggable.objects.create() for i in range(3))
        a.add_keyword('a', 'b', 'c')
        b.add_keyword('a', 'b')
        c.add_keyword('a')
        
        related_to_a = a.related_list()
        self.assertIn(b, related_to_a, 'A is linked to B')
        self.assertIn(c, related_to_a, 'A is linked to C')
        self.assertTrue(related_to_a.index(b)<related_to_a.index(c), 'Ordered by common keywords cardinal')
    
    
    def test_polymorph(self):
        """Polymorphism handling and performances"""
        ulb = Category.objects.create(name="ULB", description="Universite Libre de Bruxelles")
        
        polytek = Category.objects.create(name="Polytech", description="Ecole Polytechnique")
        ulb.attach(polytek)
        ba1p = Category.objects.create(name="BA1-POLY", description="Bachelier 1 en polytech")
        polytek.attach(ba1p)
        
        science = Category.objects.create(name="FS", description="Faculte des Sciences")
        ulb.attach(science)
        ba1i = Category.objects.create(name="BA1-INFO", description="Bachelier 1 en sciences informatiques")
        science.attach(ba1i)
        
        prog = Course.objects.create(name="Programmation 1", mnemonic="INFO-F-101", teacher="tmassart@ulb.ac.be")
        ba1p.attach(prog)
        ba1i.attach(prog)
        
        self.assertIn(ba1p, prog.ancestors(), 'INFO-F-101 for polytech')
        self.assertIn(ba1i, prog.ancestors(), 'INFO-F-101 for comp. sc.')
    
