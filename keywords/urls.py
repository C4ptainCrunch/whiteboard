from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^(\d+)/related.(json|html)$', 'keywords.views.related')
)