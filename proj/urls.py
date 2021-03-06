from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('main.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^scrape/', include('scrape.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
