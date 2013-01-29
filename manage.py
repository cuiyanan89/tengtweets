#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tengtweets.settings")

    from django.core.management import execute_from_command_line
    if len(sys.argv) == 2 and sys.argv[1] == "fetch":
        import os
        lock_file = '/tmp/tengtweets_fetch_lock.tmp'
        if os.path.exists(lock_file):
            exit(0)

        from tengtweets.tweets.models import Tweet
        from tweepy import api
        import logging
        import time

        open(lock_file, 'w').close()
        logger = logging.getLogger('info')
        logger_error = logging.getLogger('error')
        count = 0
        count_zh = 0
        for i in range(5):
            tweets = api.search(lang='zh', q='*', rpp=100)
            for t in tweets:
                try:
                    if (Tweet.objects.create_tweet(t)):
                        count += 1
                        count_zh += 1
                except Exception, e:
                    logger_error.error("Error: %s id: %s text: %s" % (
                        e, t.id, t.text
                        ))
            time.sleep(8)

            tweets = api.search(lang='en', q='*', rpp=10)
            for t in tweets:
                try:
                    if (Tweet.objects.create_tweet(t)):
                        count += 1
                except Exception, e:
                    logger_error.error("Error: %s id: %s text: %s" % (
                        e, t.id, t.text
                        ))
            time.sleep(1)
        logger.info("saved %d tweets (%d zh)" % (count, count_zh))
        if os.path.exists(lock_file):
            os.remove(lock_file)
    else:
        execute_from_command_line(sys.argv)
