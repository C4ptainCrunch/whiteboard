from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^(\d+)\.?(json|html)?$', 'agora.views.index_thread'),
    (r'^(\d+)/edit/?$', 'agora.views.edit_thread'),
    (r'^(\d+)/reply/?$', 'agora.views.reply_thread'),
) + staticfiles_urlpatterns()
