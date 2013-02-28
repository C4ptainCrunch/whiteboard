from graph.models import Node, Category, Course, Thread
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        toplevel = Category.objects.create(name="P402", description="P402::Whiteboard")
        
        science = Category.objects.create(name="Fac Sciences", description="Faculte des sciences")
        toplevel.children.append(science)
        
        ba1info = Category.objects.create(name="BA1 Sc. Info", description="Bachelier 1 en Sciences Informatiques")
        science.children.append(ba1info)
        
        polytek = Category.objects.create(name="Polytech", description="Ecole polytechnique")
        toplevel.children.append(polytek)
    
