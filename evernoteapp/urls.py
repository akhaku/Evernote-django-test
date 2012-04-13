from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'account.views.home_page'),
    url(r'^login/$', 'account.views.login_page' ),
    url('^home/$', 'basic.views.landing'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'evernoteapp.views.home', name='home'),
    # url(r'^evernoteapp/', include('evernoteapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
