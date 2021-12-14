from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Post, Hello, Review


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
    post = get_object_or_404(Post, pk=pk)

    review_list = post.review_set.all()
    tag_list = post.tag_set.all()
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "review_list": review_list,
            "tag_list": tag_list,
        },
    )


def review_list(request: HttpRequest) -> HttpResponse:
    list = Review.objects.all()
    query = request.GET.get("query", "")

    if query:
        list = list.filter(title__icontains=query)

    return render(request, "blog/review_list.html", {
        "review_list": list,
    })


def review_detail(request: HttpRequest, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)

    return render(request, "blog/review_detail.html", {
        "review": review,
    })
