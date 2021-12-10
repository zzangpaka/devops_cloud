from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# /shop/new/
from shop.forms import ShopForm


# /shop/100/
from shop.models import Shop


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, "shop/shop_detail.html", {
        "shop": shop,
    })


def shop_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError("아직 만드는 중")

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            # shop_detail 뷰를 구현했다면
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form
    })