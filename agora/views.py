from graph.models import Node
from agora.models import Message, Thread, TreadForm, MessageForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django.shortcuts import render
import json

def HttpMethodNotAllowed(*allowed):
    res = HttpResponse("Method not allowed", status=405) #Method not allowed
    res['Allow'] = ','.join(allowed) #Required by HTTP1.1 protocol for 405 error
    return res


def index_thread(req, nodeid, format):
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
    if format.lower() == 'html':
        form = MessageForm()
        return render(req, 'index_thread.haml', {
            'thread':thread,
            'keywords': thread.keywords.all(),
            'message_list':thread.message_set.all().order_by('index'),
            'form': form
        })
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

def create(request,parentid):
    if request.method == 'POST':
        form = TreadForm(request.POST)
        if form.is_valid():
            thread = Thread(name=form.cleaned_data['subject'])
            thread.save()
            for tag in form.cleaned_data['tags'].split(','):
                if tag:
                    thread.add_keyword(tag.strip())
            parent = Node.objects.get(id=parentid)
            parent.attach(thread, acyclic_check=False)
            return HttpResponseRedirect(thread.canonic_url) # Redirect after POST
    else:
        form = TreadForm()
    
    return render(request, 'add_thread.html', {
        'form': form,
    })

def edit_thread(request,nodeid):
    if request.method == 'POST':
        form = TreadForm(request.POST)
        if form.is_valid():
            thread = Thread.objects.get(id=nodeid)
            thread.name = form.cleaned_data['subject']
            thread.save()
            return HttpResponseRedirect(thread.canonic_url) # Redirect after POST
    else:
        thread = Thread.objects.get(id=nodeid)
        form = TreadForm(initial={'subject': thread.name})
    
    return render(request, 'edit_thread.haml', {
        'form': form,
    })

def reply_thread(request, nodeid):
    response = HttpMethodNotAllowed('POST')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            thread = Thread.objects.get(id=nodeid)
            thread.reply(text=form.cleaned_data['text'])
            response = HttpResponseRedirect(thread.canonic_url)
        else:
            response = HttpResponse(status=400) #Bad Request
    return response
        