from graph.models import Node
from django.shortcuts import redirect

import json

def redir2graph(req):
    return redirect('/graph/static/browse.html')
