from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Profile, Post


def profile(request: HttpRequest) -> HttpResponse:
    qs = Profile.objects.all()
    return render(request, "blog/profile.html", {
        "profile": qs,
    })


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "blog/post_list.html", {
        "post_list": qs,
    })

