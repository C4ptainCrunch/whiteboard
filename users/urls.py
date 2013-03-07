from django.conf.urls import patterns, include, url
from users.views import intraAuth

urlpatterns = patterns('',
    (r'^auth$', 'users.views.intraAuth'),
    (r'su/(\w+)$', 'users.views.admin_auth'),
    (r'^login$', 'users.views.user_login'),
    (r'^logout$', 'users.views.user_logout'),
    (r'^$', 'users.views.profile'),
)
