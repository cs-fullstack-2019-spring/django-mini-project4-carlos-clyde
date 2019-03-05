from django import forms

from django.forms import ModelForm
from .models import UserModel


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ["username", "password1", 'password2', 'dateaccountcreated', 'rank', ]