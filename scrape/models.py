import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Max
from django.utils import timezone

from main.models import TimeStampedModel, SaveSlug


class ScrapeSite(SaveSlug):
    '''
    information about the sites that we're scraping
    '''
    active = models.BooleanField(default=True)
    url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('scrape_site', kwargs={'pk':self.id})

    def last_scraped(self):
        site_log = ScrapeLog.objects.filter(site=self)
        return Max(site_log.create_date)


class ScrapeLogManager(models.Manager):
    def duration(self):
        duration = end_datetime - create_date
        return duration


class ScrapeLog(TimeStampedModel):
    '''
    details of each individual scrape attempt
    '''
    LOG_STATUS = (
        ('S', 'Success'),
        ('W', 'Warn'),
        ('E', 'Error'),
    )

    site = models.ForeignKey(ScrapeSite)
    status = models.CharField(max_length=1)
    message = models.CharField(max_length=255)
    end_datetime = models.DateTimeField(null=True)
    pages_detected = models.IntegerField(null=True)
    pages_scraped = models.IntegerField(null=True)

    objects = ScrapeLogManager()
