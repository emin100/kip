from django import forms
from django.contrib.auth.models import User
import pytz


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    persistent = forms.BooleanField(label="Remember this browser.", required = False)