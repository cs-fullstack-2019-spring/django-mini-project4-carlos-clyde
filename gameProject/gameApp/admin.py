from django.contrib import admin

from .models import GameModel, UserModel

admin.site.register(GameModel)
admin.site.register(UserModel)