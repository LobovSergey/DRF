from django.contrib import admin

from user.models.user_model import User, Location

admin.site.register(User)
admin.site.register(Location)
