from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)/?$', 'agora.views.thread')
) + staticfiles_urlpatterns()
