from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import LoginForm


login = LoginView.as_view(
    form_class=LoginForm,
    template_name="accounts/login_form.html",
)


signup = CreateView.as_view(
    form_class=UserCreationForm,
    success_url=reverse_lazy("accounts:login"),
    template_name="accounts/signup_form.html"
)


profile = login_required(TemplateView.as_view(
    template_name="accounts/profile.html"
))


logout = LogoutView.as_view(
    next_page="root",
)
