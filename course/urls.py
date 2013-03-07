from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)\.?(json|html)?$', 'course.views.getCourse')
) + staticfiles_urlpatterns()
