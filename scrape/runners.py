import requests

from bs4 import BeautifulSoup


class WebRunner(object):
    url = ""
    
    def get_soup(self):
        soup = BeautifulSoup(self.url)
        return soup

    def get_base_page(self):
        '''
        get the base page. this is typically the home page of the website
        '''
        request = requests.get(self.url)
        self.soup = BeautifulSoup(Request)


class StepsOfATraveler(WebRunner):
    '''
    Run for Steps Of A Traveler blog. This blog does not have separate sections
    filterd on topics/countries and we need to parse through and find any
    categorization
    '''

    url = "http://www.travelblogwave.com/stepsofatraveler/"

    def get_sections(self, klass):
        '''
        get the sections. Sections can include blogs that are already filtered by
        topic or by country.
        '''
        section_class = ""
        return 

    def get_group_pages(self):
        '''
        get the paged pages with multiple blog articles within section
        '''
        pass

    def get_article_pages(self):
        '''
        get the indiviudual pages. Each page will have multiple pages. Go through and
        get the individual page URLs
        '''
        pass

    
    def get_data(self):
        '''
        get the data. Parse through the article page and extract the data that we want
        to store.
        '''
        return self.get_base_url()

    def store_data(self):    
        '''
        store the data. Determine if we want to store the data, and which data to store.
        '''
        pass

