# encoding: utf-8
from django import forms

from models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('signed_at', 'is_active', 'confirmation_key')

    def save_if_new(self):
        self.full_clean()
        # verify if subscription was previously submited.
        q = Subscription.objects.filter(email=self.data['email'])
        if q:
            instance = q.get()
        else:
            instance = self.save()
        return instance
