# -*- coding UTF-8 -*-
from django.db import models

from utils import generate_confirmation_key


class Subscription(models.Model):
    """
    PythonCampus's subscription
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    signed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    confirmation_key = models.CharField(max_length=40)

    class Meta:
        ordering = ['name', 'signed_at']

    def __unicode__(self):
        return "%s - %s" % (self.name, self.email)

    def save(self, *args, **kwargs):
        # create a confirmation_key
        if not self.confirmation_key:
            self.confirmation_key = generate_confirmation_key(self.email)

        return super(Subscription, self).save(*args, **kwargs)
