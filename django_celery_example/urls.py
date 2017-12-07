from django.conf.urls import include, url
from django.contrib import admin

from tweets import urls as tweet_urls


urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^accounts/', include('allauth.urls')),
        url(r'^', include(tweet_urls)),
]
