from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "email"]


class LoginForm(AuthenticationForm):
    pass