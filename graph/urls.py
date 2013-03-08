from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)\.?(html|json)?$', 'graph.views.getNode'),
    (r'^(\d+)/short\.?(html|json)?$', 'graph.views.getNodeShort'),
) + staticfiles_urlpatterns()