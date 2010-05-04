from django.conf import settings
from django.conf.urls.defaults import *
from shortcuts import route
from views import new, create, index, confirm_email


urlpatterns = patterns('',
    route(r'inscricao/$', GET=new, POST=create, name='signup'),
    url(r'inscricao/confirmar/(\w+)/$', confirm_email, name='confirm_email'),
)
