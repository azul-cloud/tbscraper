import requests

from bs4 import BeautifulSoup


class WebRunner(object):
    '''
    Base class that defines the default actions shared by all web runners
    '''

    url = ""
    section_pages = []
    group_pages = []
    article_pages = []
    data = []

    def __init__(self):
        if self.url:
            self.request = requests.get(self.url)
            self.soup = BeautifulSoup(self.request.content)
        else:
            raise NotImplementedError("You must provide a url")

        self.set_sections()
        self.set_group_pages()
        self.set_article_pages()

    def __str__(self):
        return self.url


class StepsOfATravelerMixin(WebRunner):
    '''
    Run for Steps Of A Traveler blog. This blog does not have separate sections
    filterd on topics/countries and we need to parse through and find any
    categorization
    '''

    url = "http://www.travelblogwave.com/stepsofatraveler/"

    def set_sections(self):
        '''
        get the sections. Sections can include blogs that are already filtered by
        topic or by country.
        '''
        self.sections = []

    def set_group_pages(self):
        '''
        get the paged pages with multiple blog articles within section
        '''
        group_pages = self.soup.find("ul", class_="pagination")
        # page_raw_links = pagination_container.find('a')

        self.group_pages = group_pages

    def set_article_pages(self):
        '''
        get the indiviudual pages. Each page will have multiple pages. Go through and
        get the individual page URLs
        '''
        self.article_pages = []

    def get_data(self):
        '''
        get the data. Parse through the article page and extract the data that we want
        to store.
        '''
        self.data = []

    def store_data(self):    
        '''
        store the data. Determine if we want to store the data, and which data to store.
        '''
        pass


    def get_context_data(self, **kwargs):
        # add to the context data
        context = super(StepsOfATravelerMixin, self).get_context_data(**kwargs)
        context['soup'] = self.soup
        return context

