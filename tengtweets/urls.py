from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tengtweets.views.home', name='home'),
    # url(r'^tengtweets/', include('tengtweets.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
