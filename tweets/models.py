from django.conf import settings
from django.db import models
from django.urls import reverse


class Tweet(models.Model):
    twitter_id = models.BigIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.TextField()
    saved_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        dates = "{}".format(self.saved_at)
        if self.posted_at:
            dates = "{}, {}".format(dates, self.posted_at)
        return "{} - {} ({})".format(self.status, self.twitter_id, dates)

    def get_absolute_url(self):
        return reverse('tweet_detail', args=[str(self.id)])
