from graph.models import Node
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

import json

def getNode(req, nodeid):
    """
    GET /graph/<nodeid>
    => {
        'id' : int, 
        'name' : str, 
        'type' : str, 
        'children' : list[{'id':int, 'name':str, 'type':str}, ...], 
        ... 
    }
    """
    node = get_object_or_404(Node, pk=nodeid)
    return HttpResponse(json.dumps(node.to_dict(True)), content_type="application/json")


def getNodeShort(req, nodeid):
    """
    GET /graph/<nodeid>
    => {
        'id' : int, 
        'name' : str, 
        'type' : str, 
        'children' : list[{'id':int, 'name':str, 'type':str}, ...], 
        ... 
    }
    """
    node = get_object_or_404(Node, pk=nodeid)
    return HttpResponse(json.dumps(node.to_dict(False)), content_type="application/json")

