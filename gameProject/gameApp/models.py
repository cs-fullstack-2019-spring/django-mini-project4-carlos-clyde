from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GameModels(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    dateaccountcreate = models.DateField()
    rank = models.IntegerField(max_length=2,)
    course_teacher = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)