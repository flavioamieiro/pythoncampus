from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet

__all__ = ['TalksView']

class TalksView(TestCase):

    def test_talks_queryset_should_be_in_context(self):
        response = self.client.get(reverse('talks'))

        self.assertTrue(
            isinstance(response.context['talks'], QuerySet)
        )
