from django.conf.urls import patterns, include, url

from . import views


prefix = "blog_"

urlpatterns = patterns('',
    url(r'article/$', views.ArticleDetailView.as_view(), name=prefix + "article"),
    url(r'topic/$', views.ArticleTopicListView.as_view(), name=prefix + "topic"),
    url(r'country/$', views.ArticleCountryListView.as_view(), name=prefix + "country"),
    url(r'$', views.BlogArticleListView.as_view(), name=prefix + "blog"),
)
