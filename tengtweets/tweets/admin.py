from django.contrib import admin
from tengtweets.tweets.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'text', 'source')
    search_fields = ('from_user', 'from_user_name', 'text')
    list_filter = ('iso_language_code', 'created_at')

admin.site.register(Tweet, TweetAdmin)
