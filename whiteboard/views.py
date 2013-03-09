from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Context, loader

import json

def index(req):
    template = loader.get_template('index.haml')
    return HttpResponse(template.render(Context({})))


def redir2graph(req):
    return redirect('/graph/static/graph.svg')
