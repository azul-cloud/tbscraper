import requests

from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from bs4 import BeautifulSoup

from .models import ScrapeLog


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
