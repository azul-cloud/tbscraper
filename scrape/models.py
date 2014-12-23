from django.db import models

from main.models import TimeStampedModel, SaveSlug


class ScrapeSite(SaveSlug):
    '''
    information about the sites that we're scraping
    '''

    def __str__(self):
        return self.title


class ScrapeLog(TimeStampedModel):
    '''
    details of each individual scrape attempt
    '''
    site = models.ForeignKey(ScrapeSite)