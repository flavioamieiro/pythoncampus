from django.shortcuts import render_to_response
from models import Talk

def index(request):
    talks = Talk.objects.all()
    return render_to_response('talks/index.html', {'talks': talks})
