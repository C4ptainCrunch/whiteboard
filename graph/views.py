from graph.models import Node
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

import json

def node(req, nodeid):
    node = get_object_or_404(Node, pk=nodeid)
    return HttpResponse(json.dumps(node.to_dict()), content_type="application/json")


def short(req, nodeid):
    node = get_object_or_404(Node, pk=nodeid)
    return HttpResponse(json.dumps(node.short_dict()), content_type="application/json")
