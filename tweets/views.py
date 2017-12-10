from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView

from tweets.tasks import post_tweet
from tweets import models as tweet_models


class TweetCreateView(LoginRequiredMixin, CreateView):

    model = tweet_models.Tweet
    fields = ['status']

    def form_valid(self, form):
        """If the form is valid, set the logged-in user and save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        access_token = self.request.session['oauth_api.twitter.com_access_token']
        post_tweet.delay(self.request.user.id, access_token, self.object.id)

        return super().form_valid(form)


class TweetDetailView(LoginRequiredMixin, DetailView):

    model = tweet_models.Tweet
    fields = ['status', 'saved_at', 'posted_at']
