import os
import subprocess

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from tengtweets.tweets.models import Tweet

def home(request):
    total_tweets = Tweet.objects.count()
    total_tweets_zh = Tweet.objects.filter(iso_language_code='zh').count()
    log_path = os.path.join(settings.PROJECT_ROOT, 'logs/info.log')
    cmd = ['tail', '-n', '20', log_path]
    last_updates = subprocess.check_output(cmd)
    context = {
        'total_tweets': total_tweets,
        'last_updates': last_updates.replace('\n', '<br>'),
        'total_tweets_zh': total_tweets_zh,
    }
    return render(request, 'tweets/home.html', context)

def search(request):
    context = {}
    if request.method == "POST":
        q = request.POST.get("q", "")
        tweets = Tweet.objects.filter(Q(text__icontains=q) | Q(from_user=q))[:100]
        context['tweets'] = tweets
    return render(request, 'tweets/search.html', context)
