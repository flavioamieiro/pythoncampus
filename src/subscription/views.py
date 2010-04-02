from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

from models import Subscription
from forms import SubscriptionForm
from utils import send_email_confirmation


def new(request):
    form = SubscriptionForm()
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'form': form
    }
    return render_to_response('subscription/form.html', context)

def create(request):
    form = SubscriptionForm(request.POST)
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'form': form
    }
    try:
        subscription = form.save_if_new()
        send_email_confirmation(subscription)
    except ValueError:
        return render_to_response('subscription/form.html', context)
    return render_to_response('subscription/signed.html', context)

def index(request):
    subscription = Subscription.objects.filter(is_active=True)
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'subscription': subscription
    }
    return render_to_response('subscription/list.html', context)

def confirm_email(request, confirmation_key):
    try:
        subscription = Subscription.objects.get(
            confirmation_key=confirmation_key
        )
        subscription.is_active = True
        subscription.save()
    except Subscription.DoesNotExist:
        raise Http404

    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'subscription': subscription,
    }
    return render_to_response('subscription/confirmed.html', context)

