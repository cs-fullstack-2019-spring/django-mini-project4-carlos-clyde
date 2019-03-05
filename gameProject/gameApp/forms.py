from django import forms

from django.forms import ModelForm
from .models import UserModel


class NewUserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'