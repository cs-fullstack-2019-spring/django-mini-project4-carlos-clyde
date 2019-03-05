from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    dateaccountcreated = models.DateField()
    rank = models.IntegerField(max_length=2,)
    user_model = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)



class GameModel(models.Model):
    name = models.CharField(max_length=20)
    delovper = models.CharField(max_length=10)
    dateaccountmade = models.DateField()
    ageLimit = models.IntegerField(max_length=2,)
    game_model = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)