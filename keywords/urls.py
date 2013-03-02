from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^(\d+)/related$', 'keywords.views.related')
)