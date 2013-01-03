import os
import subprocess

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from tengtweets.tweets.models import Tweet

def home(request):
    total_tweets = Tweet.objects.count()
    log_path = os.path.join(settings.PROJECT_ROOT, 'logs/info.log')
    cmd = ['tail', '-n', '40', log_path]
    last_updates = subprocess.check_output(cmd)
    newest_tweets_en = Tweet.objects.filter(iso_language_code='en').order_by("-id")[:10]
    newest_tweets_zh = Tweet.objects.filter(iso_language_code='zh').order_by("-id")[:10]
    context = {
        'total_tweets': total_tweets,
        'last_updates': last_updates.replace('\n', '<br>'),
        'newest_tweets_zh': newest_tweets_zh,
        'newest_tweets_en': newest_tweets_en,
    }
    return render(request, 'tweets/home.html', context)
