from agora.models import Message, Thread
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

import json

def thread(req, nodeid):
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
    res = [msg.to_dict() for msg in Message.objects.filter(thread=thread)]
    return HttpResponse(json.dumps({'messages':res, 'node':thread.short_dict()}), content_type="application/json")

