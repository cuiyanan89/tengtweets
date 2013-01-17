from django.conf.urls import patterns, url

urlpatterns = patterns('tengtweets.tweets.views',
    url(r'^$', 'home', name='tweets_home'),
    url(r'^search/', 'search', name='tweets_search'),
)
