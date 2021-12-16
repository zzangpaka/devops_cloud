from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from PIL import Image

from accounts.forms import LoginForm, SignupForm


login = LoginView.as_view(
    form_class=LoginForm,
    template_name="accounts/login_form.html",
)



def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = SignupForm()

    return render(request, "accounts/signup_form.html", {
        "form": form,
    })


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/profile.html",)


logout = LogoutView.as_view(
    next_page="root",
)
