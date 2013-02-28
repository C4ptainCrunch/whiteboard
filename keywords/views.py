from keywords.models import Keyword
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def related(request, kwid, format):
    """Return Graph Nodes id's related to this keyword"""
    return HttpResponse('Not Implemented !', status=501)
