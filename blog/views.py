from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Article, Blog


class ArticleDetailView(TemplateView):
    '''
    Display a single blog article.
    '''
    template_name = "blogcontent/article.html"


class BlogArticleListView(TemplateView):
    '''
    display a list of the posts of a certain blog. This acts as the "home page"
    for a blog partner
    '''
    template_name = "blogcontent/blog.html"


class ArticleTopicListView(TemplateView):
    '''
    display a list of the posts for a certain topic.
    '''
    template_name = "blogcontent/topic.html"


class ArticleCountryListView(TemplateView):
    '''
    display a list of the posts of a certain country.
    '''
    template_name = "blogcontent/country.html"