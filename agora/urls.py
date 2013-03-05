from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)\.(json|html)?$', 'agora.views.thread')
) + staticfiles_urlpatterns()
