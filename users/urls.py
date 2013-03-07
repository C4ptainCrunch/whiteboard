from django.conf.urls import patterns, include, url
from users.views import intraAuth

urlpatterns = patterns('',
    (r'^auth$', 'users.views.intraAuth'),
    (r'admin$', 'users.views.admin_auth'),
    (r'^login$', 'users.views.user_login'),
    (r'^$', 'users.views.profile'),
)
