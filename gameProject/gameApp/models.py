from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    dateaccountcreated = models.DateField()
    # rank = models.IntegerField(max_length=2,)
    user_key = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

def __str__(self):
    return self.username

class GameModel(models.Model):
    name = models.CharField(max_length=20)
    developer = models.CharField(max_length=10)
    dateaccountmade = models.DateField()
    # ageLimit = models.IntegerField(max_length=2,)
    game_key = models.ForeignKey(UserModel, on_delete=models.PROTECT, null=True, blank=True)


def __str__(self):
    return self.name