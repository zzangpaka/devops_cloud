from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from blog.forms import PostForm, ReviewForm
from blog.models import Post, Hello, Review


def hello(request: HttpRequest) -> HttpResponse:
    hello = Hello.objects.all()

    return render(request, "blog/hello.html", {
        "profile": hello
    })


def post_list(request: HttpRequest) -> HttpResponse:
    list = Post.objects.all()

    query = request.GET.get("query", "")
    conditions = Q(title__icontains=query) | Q(author_name__icontains=query)

    if query:
        list = list.filter(conditions)

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


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            return redirect(saved_post)
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {
        "form": form,
    })


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            saved_post = form.save()
            return redirect(saved_post)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_form.html", {
        "form": form,
        "post": post,
    })


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html",{
        "post": post,
    })


def review_list(request: HttpRequest) -> HttpResponse:
    list = Review.objects.all()

    query = request.GET.get("query", "")
    conditions = Q(title__icontains=query) | Q(author_name__icontains=query)

    if query:
        list = list.filter(conditions)

    return render(request, "blog/review_list.html", {
        "review_list": list,
    })


def review_detail(request: HttpRequest, pk: int) -> HttpResponse:

    review = Review.objects.get(pk=pk)

    return render(request, "blog/review_detail.html", {
        "review": review,
    })


def review_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            saved_review = form.save()
            return redirect(saved_review)
    else:
        form = ReviewForm()

    return render(request, "blog/review_form.html", {
        "form": form,
    })


def review_edit(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            saved_review = form.save()
            return redirect(saved_review)
    else:
        form = ReviewForm(instance=review)

    return render(request, "blog/review_form.html", {
        "form": form,
        "review": review,
    })


def review_delete(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        review.delete()
        return redirect("blog:review_list")

    return render(request, "blog/review_confirm_delete.html",{
        "review": review,
    })
