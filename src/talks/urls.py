# -*- coding: utf-8 -*-
from django.conf.urls.defaults import include, patterns, url


urlpatterns = patterns('talks.views',
    url(r'^$', 'index', name='talks'),
    url(r'^details/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[^/]+)', 'details', name='details'),
)
