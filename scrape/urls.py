from django.conf.urls import patterns, include, url

from . import views


prefix = "scrape_"

urlpatterns = patterns('',
    url(r'admin/$', views.ScrapeAdminTemplateView.as_view(), name=prefix + "admin"),
    url(r'log/$', views.ScrapeLogListView.as_view(), name=prefix + "logs"),
)
