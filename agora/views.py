from agora.models import Message, Thread
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
import json


def response(format, thread):
    if format and format.lower() == 'html':
        template = loader.get_template('threadIndex.haml')
        return HttpResponse(template.render(Context({
            'thread':thread, 
            'keywords': thread.keywords.all(), 
            'message_list':thread.message_set.all().order_by('index')
        })))
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
    if not format or len(format)==0:
        format = 'json' if req.is_ajax() else 'html'
    thread = get_object_or_404(Thread, pk=nodeid)
    return response(format, thread)

