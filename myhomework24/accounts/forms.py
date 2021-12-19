from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class Signup(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "email"]


class LoginForm(AuthenticationForm):
    pass