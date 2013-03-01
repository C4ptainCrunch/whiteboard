from graph.models import Node
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

import json

def node(req, nodeid):
    node = get_object_or_404(Node, pk=nodeid)
    return HttpResponse(json.dumps(node.to_dict()))


def names(req, nodes):
    res = list(Node.objects.values('id', 'name').filter(id__in=nodes.split('-')))
    for i in range(len(res)):
        res[i]['name'] = str(res[i]['name']) #Avoid JSON errors
    return HttpResponse(json.dumps({'nodes':res}))
