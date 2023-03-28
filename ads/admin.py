from django.contrib import admin

from ads.models.ads_model import Announcement, Category

admin.site.register(Announcement)
admin.site.register(Category)
