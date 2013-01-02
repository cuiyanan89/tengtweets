from django.test import TestCase
from tengtweets.tweets.models import Tweet
from tweepy import api

class GenericTest(TestCase):
    def test_save_tweets(self):
        tweets = api.search(lang='zh', q='*')
        for t in tweets:
            print t.text
            Tweet.objects.create_tweet(t)
        self.assertTrue(Tweet.objects.count() > 10)
