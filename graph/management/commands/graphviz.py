from graph.models import Node, Category, Course
from agora.models import Thread
from keywords.models import Keyword
from django.core.management.base import BaseCommand
from optparse import make_option

class Command(BaseCommand):
    COLORS = {
        Node : 'grey',
        Category: 'lightblue',
        Course: 'gold',
        Thread: 'coral'
    }
    
    help = """
    Export the main graph to graphviz format
    see also: http://www.graphviz.org/Documentation.php
    Use in combination with dot (or circo, neato, twopi, ...)
    manage.py graphviz | dot -Tpng > graph.png
    """
    
    option_list = BaseCommand.option_list + (
        make_option('-u', '--urlprefix',
            action='store',
            dest='urlprefix',
            default="http://localhost:8000",
            help='URL prefix for clickable nodes'
        ),
    )
    
    def handle(self, *args, **options):
        f = self.stdout
        f.write('digraph P402 {\n')
        for node in Node.objects.all():
            color = self.COLORS.get(type(node), 'black')
            url = options['urlprefix'] + '/graph/%d'%(node.pk)
            f.write('\t%d [style=filled label="%s" fillcolor=%s URL="%s"]\n'%(node.pk, str(node.name), color, url))
            for child in node.children():
                f.write('\t%d -> %d;\n'%(node.pk, child.id))
        
        #Color legend
        f.write('edge [style=invis];\n')
        for klass in self.COLORS:
            f.write('\t"%s" [style=filled,fillcolor=%s,shape=box,margin="0,0",width=1,height=0.5,arrow=none]'%(klass().classBasename(), self.COLORS[klass]))
        i = 0
        for klass in self.COLORS:
            if i>0: f.write(' -> ')
            f.write('"'+klass().classBasename()+'"')
            i += 1
        f.write('}\n')