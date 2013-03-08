from django.conf.urls import patterns, include, url
from users.views import intraAuth
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^auth$', 'users.views.intraAuth'),
    (r'su/(\w+)$', 'users.views.admin_auth'),
    (r'^login$', TemplateView.as_view(template_name="login.html")),
    (r'^ulb$', 'users.views.user_login'),
    (r'^logout$', 'users.views.user_logout'),
    (r'^$', 'users.views.profile'),
)
