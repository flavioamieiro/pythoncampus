import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Talk

def index(request):
    talks = Talk.objects.order_by('start_time')
    return render_to_response('talks/index.html', RequestContext(request, {'talks': talks}))

def details(request, year, month, day, slug):
    dates = [int(x) for x in [year, month, day]]
    talk = Talk.objects.get(day=datetime.date(*dates), slug=slug)
    return render_to_response('talks/details.html', RequestContext(request, {'talk': talk}))
