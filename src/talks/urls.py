# -*- coding: utf-8 -*-
from django.conf.urls.defaults import include, patterns, url


urlpatterns = patterns('talks.views',
    url('^$', 'index', name='talks'),
)
