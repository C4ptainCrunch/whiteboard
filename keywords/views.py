from keywords.models import Keyword
from graph.models import Thread
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

def related(request, kwid):
    """Return Graph Nodes id's related to this keyword"""
    keyword = get_object_or_404(Keyword, pk=kwid)
    res = list(Thread.objects.values('id', 'name').filter(keywords=keyword))
    for i in range(len(res)):
        res[i]['name'] = str(res[i]['name'])
    return HttpResponse(json.dumps({'nodes':res}))
