from agora.models import Message, Thread
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

def renderHTML(thread):
    raise NotImplemented()


def response(format, thread):
    if format.lower() == 'html':
        return HttpResponse(renderHTML(thread), content_type="text/html")
    else:
        obj = {
            'id' : thread.pk,
            'name': thread.name,
            'keywords': [
                {'id':kw.pk, 'name':kw.name} for kw in thread.keywords.all()
            ],
            'messages': [
                {'index':msg.index, 'text':msg.text, 'posted':str(msg.posted)} for msg in thread.message_set.all()
            ]
        }
        return HttpResponse(json.dumps(obj), content_type="application/json")


def thread(req, nodeid, format):
    """
    GET /agora/<nodeid>
    => {
        'messages': [
            {'index':int, 'posted':datetime, },
            ...
        ]
    }
    """
    thread = get_object_or_404(Thread, pk=nodeid)
    return response(format, thread)
    #res = [msg.to_dict() for msg in Message.objects.filter(thread=thread)]
    #return HttpResponse(json.dumps({'messages':res, 'node':thread.short_dict()}), content_type="application/json")

