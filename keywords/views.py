from keywords.models import Keyword
from graph.models import Thread
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

def related(request, kwid):
    """Return Graph Nodes id's and names related to this keyword"""
    keyword = get_object_or_404(Keyword, pk=kwid)
    res = []
    for thread in keyword.thread_set.all():
        res.append(thread.short_dict())
    return HttpResponse(json.dumps({'nodes':res}))
