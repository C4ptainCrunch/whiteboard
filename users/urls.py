from django.conf.urls import patterns, include, url
from users.views import intraAuth

urlpatterns = patterns('',
    (r'^auth$', 'users.views.intraAuth'),
    (r'^login$', 'users.views.login'),
    (r'admin$', 'users.views.admin_auth'),
)
