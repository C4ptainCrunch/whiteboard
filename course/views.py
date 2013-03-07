from course.models import Course

from django.shortcuts import get_object_or_404
from django.template import Context, loader
from django.http import HttpResponse
import json

def response(format, course):
    if format and format.lower() == 'html':
        template = loader.get_template('course.haml')
        return HttpResponse(template.render(Context({'course':course})))
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

def getCourse(req, nodeid, format):
    if not format or len(format)==0:
        format = 'json' if req.is_ajax() else 'html'
    course = get_object_or_404(Course, pk=nodeid)
    return response(format, course)

