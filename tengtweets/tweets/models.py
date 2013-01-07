from django.db import models
from django.utils.timezone import utc
import json
from tengtweets.tweets.utils import unescape

class TweetManager(models.Manager):
    def create_tweet(self, t):
        if self.filter(pk=t.id).exists():
            return False
        text = unescape(t.text)
        if len(text) > 170:
            raise ValueError("Text too long")

        if t.geo:
            geo = json.dumps(t.geo)
        else:
            geo = ''
        created_at = t.created_at.replace(tzinfo=utc)
        tweet = self.model(
            id = t.id,
            created_at = created_at,
            from_user = t.from_user,
            from_user_id = t.from_user_id,
            from_user_name = t.from_user_name,
            geo = geo,
            iso_language_code = t.iso_language_code or '',
            source = t.source,
            text = text,
            to_user = t.to_user or '',
            to_user_id = t.to_user_id or 0,
            to_user_name = t.to_user_name or '',
        )
        tweet.save()
        return True


class Tweet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    from_user = models.CharField(max_length=40)
    from_user_id = models.BigIntegerField()
    from_user_name = models.CharField(max_length=40)
    geo = models.CharField(max_length=256, blank=True)
    iso_language_code = models.CharField(max_length=8)
    source = models.CharField(max_length=64)
    text = models.CharField(max_length=170) # RT @someone: 140 chars
    to_user = models.CharField(max_length=40, blank=True)
    to_user_id = models.BigIntegerField(default=0)
    to_user_name = models.CharField(max_length=40)

    objects = TweetManager()

    def __unicode__(self):
        return u"@%s: %s" % (self.from_user, self.text)
