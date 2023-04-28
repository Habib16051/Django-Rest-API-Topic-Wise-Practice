from django import forms
from django.contrib.auth.models import User
from .models import UserInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserInfoform(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('facebook_id', 'profile_pic')
