from django.views.generic import CreateView

from tweets import models as tweet_models


class TweetCreateView(CreateView):

    model = tweet_models.Tweet
    fields = "__all__"
