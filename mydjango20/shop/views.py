from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# /shop/new/
from shop.forms import ShopForm, ReviewForm


# /shop/100/
from shop.models import Shop, Review, Category, Tag


def shop_list(request: HttpRequest) -> HttpResponse:
    category_qs = Category.objects.all()
    qs = Shop.objects.all() # .order_by("-id") -> 대신 model에서 ordering으로 지정

    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    return render(request, "shop/shop_list.html", {
        "category_list": category_qs,
        "shop_list": qs,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    review_list = shop.review_set.all()
    tag_list = shop.tag_set.all()

    return render(request, "shop/shop_detail.html",
        {
            "shop": shop,
            "review_list": review_list,
            "tag_list": tag_list,
        },
    )


def shop_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError("아직 만드는 중")

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, "성공적으로 등록했습니다.")
            # shop_detail 뷰를 구현했다면
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            edit_post = form.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect("shop:shop_detail", edit_post.pk)
    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_form.html", {
        "form": form
    })


def review_new(request: HttpRequest, shop_pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=shop_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.save()
            messages.success(request, "성공적으로 등록했습니다.")
            return redirect("shop:shop_detail", shop_pk)
    else:
        form = ReviewForm()
    return render(request, "shop/review_form.html", {
        "form": form,
    })


def review_edit(request: HttpRequest, shop_pk: int, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            edit_review = form.save()
            edit_review.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect("shop:shop_detail", shop_pk)
    else:
        form = ShopForm(instance=review)

    form = ReviewForm(instance=review)
    return render(request, "shop/review_form.html", {
        "form": form,
    })


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:
    qs = Shop.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(
        request,
        "shop/tag_detail.html",
        {
            "tag_name": tag_name,
            "shop_list": qs,
        }
    )
