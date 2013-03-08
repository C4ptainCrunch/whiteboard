from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^keywords/', include('keywords.urls')),
    (r'^graph/', include('graph.urls')),
    (r'^category/', include('graph.urls')),
    (r'^thread/', include('agora.urls')),
    (r'^course/', include('course.urls')),
    (r'^/?$', 'whiteboard.views.redir2graph'),
    # Examples:
    # url(r'^$', 'whiteboard.views.home', name='home'),
    # url(r'^whiteboard/', include('whiteboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)