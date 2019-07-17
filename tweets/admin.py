from django.contrib import admin

from tweets import models


admin.site.register(models.RecentTweetCount)
admin.site.register(models.Tweet)
