from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)$', 'graph.views.node'),
    (r'^names/([\d-]+)', 'graph.views.names')
) + staticfiles_urlpatterns()