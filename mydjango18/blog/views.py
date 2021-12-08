from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Profile


def profile(request: HttpRequest) -> HttpResponse:
    qs = Profile.objects.all()
    return render(request, "blog/profile.html", {
        "profile": qs,
    })