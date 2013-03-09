from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)\.?(json|html)?$', 'agora.views.thread'),
    (r'^new/(\d+)$', 'agora.views.add_thread'),
    (r'^edit/(\d+)$', 'agora.views.edit_thread'),
) + staticfiles_urlpatterns()
