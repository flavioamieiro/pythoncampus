# -*- coding UTF-8 -*-

from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=75)
    url = models.URLField(verify_exists=False, blank=True)
    email = models.EmailField()
    description = models.TextField()
    photo_url = models.URLField(verify_exists=False)

    def __unicode__(self):
        return self.name

class Talk(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    day = models.DateField(blank=True)
    start_time = models.TimeField(blank=True)
    duration = models.CharField(max_length=20, blank=True)
    place = models.CharField(max_length=20, blank=True)
    speaker = models.ForeignKey(Speaker)

    media_code = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.speaker.name, self.title)
