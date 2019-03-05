from django import forms

from django.forms import ModelForm
from .models import UserModel, GameModel


class NewUserForm(ModelForm):
    class Meta:
        model = UserModel
        exclude = [" user_key"]
        fields = '__all__'


    def passwordCheck(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords must match.")

        return cleaned_data


class NewGameForm(ModelForm):
        class Meta:
            model = GameModel
            exclude = [" game_key"]
            fields = '__all__'