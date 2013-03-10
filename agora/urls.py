from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)\.?(json|html)?$', 'agora.views.thread'),
    (r'^(\d+)/edit/?$', 'agora.views.edit_thread'),
) + staticfiles_urlpatterns()
