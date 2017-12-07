from django.contrib import admin

from tweets import models


admin.site.register(models.Tweet)
