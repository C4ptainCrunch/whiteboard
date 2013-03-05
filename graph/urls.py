from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)/?$', 'graph.views.node'),
    (r'^(\d+)/short/?$', 'graph.views.short'),
) + staticfiles_urlpatterns()