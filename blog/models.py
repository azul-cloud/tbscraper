from django.db import models

from main.models import SaveSlug


class Blog(SaveSlug):
    '''
    Stores Blog Objects. For each blog we're going to go to their 
    site and scrape their articles.
    '''
    def __str__(self):
        return self.title

class Article(SaveSlug):
    '''
    Stores the individual articles for a blog
    '''
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.title