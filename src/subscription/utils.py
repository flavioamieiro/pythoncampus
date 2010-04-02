from datetime import datetime, timedelta
from random import random
 
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site 
from django.template.loader import render_to_string
from django.utils.hashcompat import sha_constructor
from django.core.mail import send_mail
from django.conf import settings


def generate_confirmation_key(email):
    salt = sha_constructor(str(random())).hexdigest()[:5]
    return sha_constructor(salt + email).hexdigest()

def generate_activate_url(confirmation_key):
    current_site = Site.objects.get_current()
    path = reverse("confirm_email", args=[confirmation_key])
    return u"http://%s%s" % (unicode(current_site.domain), path)

def send_email_confirmation(subscription):
    context = {
        "name": subscription.name,
        "activate_url": generate_activate_url(subscription.confirmation_key),
        "confirmation_key": subscription.confirmation_key,
    }
    subject = render_to_string("subscription/mail_subject.txt", context)
    message = render_to_string("subscription/mail_message.txt", context)
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
              [subscription.email, settings.DEFAULT_FROM_EMAIL])
