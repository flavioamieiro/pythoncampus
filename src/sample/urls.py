# -*- coding: utf-8 -*-
from django.conf.urls.defaults import include, patterns, url


urlpatterns = patterns('views',
    url('^$', 'index', name='index'),
    url('^new/$', 'new', name='new'),
    url('^(?P<id>\d+)/edit/$', 'edit', name='edit'),
    url('^(?P<id>\d+)/delete/$', 'delete', name='delete'),
)
