from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post, Hello


def hello(request: HttpRequest) -> HttpResponse:
    hello = Hello.objects.all()

    return render(request, "blog/hello.html", {
        "profile": hello
    })


def post_list(request: HttpRequest) -> HttpResponse:
    list = Post.objects.all()
    query = request.GET.get("query", "")

    if query:
        list = list.filter(title__icontains=query)

    return render(request, "blog/post_list.html", {
        "post_list": list,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)

    return render(request, "blog/post_detail.html", {
        "post": post,
    })