from django.conf.urls.defaults import *

handler500 = 'views.server_error'
handler404 = 'views.not_found'

urlpatterns = patterns('server.views',
        (r'^404/$', 'not_found'),
        (r'^500/$', 'server_error'),
)