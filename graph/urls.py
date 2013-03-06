from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)/?$', 'graph.views.getNode'),
    (r'^(\d+)/short/?$', 'graph.views.getNodeShort'),
) + staticfiles_urlpatterns()