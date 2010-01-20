from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^palestras/', include('talks.urls')),
)

urlpatterns+= patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'about.html'}),

    (r'^sobre/$', 'direct_to_template', {'template': 'about.html'}),

    (r'^eu-quero-uma-pythoncampus-na-minha-universidade/$',
        'direct_to_template', {'template': 'i-want.html'}),

    (r'^contato/$', 'direct_to_template', {'template': 'contact.html'}),
)
