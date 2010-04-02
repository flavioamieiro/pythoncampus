import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet

from talks.models import Talk, Speaker

__all__ = ['TalksView', 'TalkDetailView']

class TalksView(TestCase):

    def test_talks_queryset_should_be_in_context(self):
        response = self.client.get(reverse('talks'))

        self.assertTrue(
            isinstance(response.context['talks'], QuerySet)
        )

class TalkDetailView(TestCase):

    def test_talk_should_be_in_context(self):

        speaker = Speaker(
            name = 'Santa Claus',
            url = 'www.north_pole.net',
            email = 'admin@north_pole.net',
        )
        speaker.save()
        talk = Talk(
            title = 'Title',
            slug = 'title',
            description = 'Description',
            day = datetime.date(2010, 1, 20),
            start_time = datetime.time(10, 10),
            duration = '1 hour',
            place = 'Room 756',
            speaker = speaker,
        )
        talk.save()

        second_talk = Talk(
            title = 'Another Title',
            slug = 'another-title',
            description = 'Another description',
            day = datetime.date(2010, 1, 22),
            start_time = datetime.time(10, 10),
            duration = '50 minutes',
            place = 'Room 765',
            speaker = speaker,
        )
        second_talk.save()

        year = '%04d' % talk.day.year
        month = '%02d' % talk.day.month
        day = '%02d' % talk.day.day

        response = self.client.get(reverse('details', args=[year, month, day, talk.slug]))

        rendered_talk = response.context['talk']

        self.assertTrue(isinstance(rendered_talk, Talk))

        self.assertEquals(rendered_talk, talk)

        talk.delete()
        second_talk.delete()
        speaker.delete()
