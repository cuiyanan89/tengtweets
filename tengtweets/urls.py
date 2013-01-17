from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tengtweets.tweets.views.home', name='home'),
    url(r'^tweets/', include('tengtweets.tweets.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
