from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class ScrapeLog(ListView):
    '''
    View the details of all the individual scrape attempts
    '''
    pass


class ScrapeAdminTemplateView(TemplateView):
    '''
    Perform actions for the scraping. Initially we'll just run
    scrapes individually, but in the future we'll have the process
    more refined.
    '''
    pass
