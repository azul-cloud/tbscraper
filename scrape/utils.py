

class ScrapeRunner(object):
    '''
    this is the object that will get instantiated to scrape a
    website. Most of these properties and functions won't do anything,
    but it gives us the set structure for when we instantiate 
    ScrapeRunner objects
    '''
    def __init__(self, blog):
        self.blog = blog

        # base page is the page that has all the posts (or pagination)
        self.base_page = 
        
        # list of all the pages that contain articles (from pagination)
        self.article_group_pages = []

        # list of all the individual article pages that we will scrape
        self.article_pages = []

        # store the amount of pages that were scraped
        self.pages_scraped = 0

    def get_all_pages(self):
        '''
        this function will be called to get all the individual
        blog pages
        '''
        return True

    def log_scrape(self):
        '''
        log our scrape session
        '''
        return True