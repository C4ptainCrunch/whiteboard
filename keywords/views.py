from keywords.models import Keyword
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

def related(request, kwid):
    """Return Graph Nodes id's and names related to this keyword"""
    keyword = get_object_or_404(Keyword, pk=kwid)
    res = []
    for tagged in keyword.taggable_set.all():
        res.append(tagged.short_dict())
    return HttpResponse(json.dumps({'nodes':res}))
