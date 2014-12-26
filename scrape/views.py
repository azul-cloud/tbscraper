import requests

from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from bs4 import BeautifulSoup

from .models import ScrapeLog, ScrapeSite
from .runners import StepsOfATraveler


class ScrapeLogListView(ListView):
    '''
    View the details of all the individual scrape attempts
    '''
    model = ScrapeLog
    template_name = "scrapecontent/logs.html"


class ScrapeAdminTemplateView(TemplateView):
    '''
    Perform actions for the scraping. Initially we'll just run
    scrapes individually, but in the future we'll have the process
    more refined.
    '''
    template_name = "scrapecontent/admin.html"

    def get_context_data(self):
        obj = StepsOfATraveler()

        return {"object":obj}


class ScrapeSiteDetailView(DetailView):
    '''
    Scrape an individual site
    '''
    model = ScrapeSite
    template_name = "scrapecontent/site.html"

