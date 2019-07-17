from __future__ import absolute_import, unicode_literals
from celery import shared_task
from twitter import OAuth, Twitter

from allauth.socialaccount.models import SocialAccount
from django.utils.timezone import now

from tweets.models import Tweet


@shared_task
def post_tweet(user_id, access_token, tweet_id):
    tweet = Tweet.objects.filter(pk=tweet_id).first()
    if tweet:
        user_account = SocialAccount.objects.get(user__id=user_id)
        token = user_account.socialtoken_set.latest('expires_at')

        auth = OAuth(access_token['oauth_token'], access_token['oauth_token_secret'],
                     token.app.client_id, token.app.secret)
        twitter = Twitter(auth=auth)

        result = twitter.statuses.update(status=tweet.status)

        tweet.posted_at = now()
        tweet.twitter_id = result['id']
        tweet.save()
        return True

    return False
