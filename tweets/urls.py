from django.conf.urls import url
from django.views.generic import RedirectView

from tweets import views as tweet_views


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='tweets/add/', permanent=False)),
    url(r'^tweets/add/$', tweet_views.TweetCreateView.as_view(), name='tweet_create'),
]
