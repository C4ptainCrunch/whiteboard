from django.conf.urls import patterns, include, url
from users.views import intraAuth

urlpatterns = patterns('',
    (r'^$', 'users.views.profile'),
    (r'^auth$', 'users.views.intraAuth'),
    (r'^login$', 'users.views.login'),
)
