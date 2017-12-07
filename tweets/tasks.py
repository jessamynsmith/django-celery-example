from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.utils.timezone import now

from tweets.models import Tweet


@shared_task
def post_tweet(tweet_id):
    tweet = Tweet.objects.filter(pk=tweet_id).first()
    if tweet:
        tweet.posted_at = now()
        tweet.save()
    return False
