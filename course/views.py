from course.models import Course
from agora.models import Thread

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
import json

def getCourse(req, nodeid, format):
    if not format or len(format)==0:
        format = 'json' if req.is_ajax() else 'html'
    course = get_object_or_404(Course, pk=nodeid)
    if format.lower() == 'html':
        discussions = []
        for node in course.childrens():
            if isinstance(node, Thread): discussions.append(node)
        return render(req, 'index_course.haml', {
            'course':course,
            'discussions': discussions
        })
    else:
        obj = {
            'id' : course.pk,
            'name': course.name,
            'mnemonic' : course.mnemonic,
            'teacher' : course.teacher,
            'description': course.description,
            'last-modified': str(course.lastmodif)
        }
        return HttpResponse(json.dumps(obj), content_type="application/json")


def addThread(req, nodeid):
    course = get_object_or_404(Course, pk=nodeid)
    thread = Thread.objects.create()
    course.attach(thread)
    return HttpResponseRedirect(thread.canonic_url+'/edit')

