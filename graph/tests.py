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
        """Playing with keywords"""
        tagname = 'hoho'
        k1 = Taggable.KW(tagname)
        k2 = Taggable.KW(tagname)
        self.assertEqual(k1, k2, 'Keyword equivalence')
        k3 = Taggable.KW(tagname.upper())
        self.assertEqual(k1, k3, 'Keyword equivalence')
        k4 = Taggable.KW(tagname+'_')
        self.assertNotEqual(k1, k4, 'Keyword without equivalence')
        
        a, b, c, d = (Taggable.objects.create() for i in range(4))
        a.add_keyword('a', 'b', 'c', 'tag')
        b.add_keyword('b', 'd')
        c.add_keyword('a', 'c', 'tag')
        d.add_keyword('d')
        
        related_to_a = a.related_list()
        self.assertIn(b, related_to_a, 'A -- B')
        self.assertIn(c, related_to_a, 'A -- C')
        self.assertTrue(related_to_a.index(c)<related_to_a.index(b), 'Ordered by common keywords cardinal')
        
        self.assertNotIn(d, related_to_a, 'A -/- D')
        self.assertIn(d, b.related_list(), 'B -- D')
    
    
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
    
