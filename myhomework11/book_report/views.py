from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from book_report.models import Post



def index(request):
    return render(request, "book_report/index.html")


def post_list(request: HttpRequest) -> HttpResponse:
    # request.GET QueryString Values
    # request.POST Post 요청 Values
    # request.FILES Post 요청에서 파일 Values
    qs = Post.objects.all() # QuerySet Type
    qs = qs.order_by("-pk")

    q = request.GET.get("q", "")
    q2 = request.GET.get("q2", "")
    q3 = request.GET.get("q3", "")#.get("?", "?") : 사전형이라면 거의 다 지원
    if q:
        qs = qs.filter(genre__icontains=q) #i=대소문자 구별 안함
    elif q2:
        qs = qs.filter(book_name__icontains=q2 )
    elif q3:
        qs = qs.filter(author_name__icontains=q3)

    # blog/templates/blog/post_list.html
    return render(request, "book_report/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # pk = 1
    post = Post.objects.get(pk=pk)
    return render(request, "book_report/post_detail.html", {
        "post": post,
    })