from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from book.models import Book


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:
    qs = Book.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request, "book/tag_detail.html", {
        "tag_name": tag_name,
        "book_list": qs,
    })


def profile(request: HttpRequest) -> HttpResponse:
    return render(request, "book/profile.html")


def book_list(request: HttpRequest) -> HttpResponse:
    qs = Book.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    context_data = {
        "book_list": qs,
    }

    return render(request, "book/book_list.html", context_data)


def book_detail(request: HttpRequest, pk: int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    comment_list = book.comment_set.all()
    tag_list = book.tag_set.all()
    return render(request, "book/book_detail.html", {
        "book": book,
        "comment_list": comment_list,
        "tag_list": tag_list,
    })