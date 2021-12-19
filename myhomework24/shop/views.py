from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import resolve_url, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.forms import ShopForm, ReviewForm, DeleteForm
from shop.mixins import ReviewUserCheckMixin, ShopUserCheckMixin
from shop.models import Shop, Category, Review


class ShopListView(ListView):
    model = Shop
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["category_list"] = Category.objects.all()
        return context_data


shop_list = ShopListView.as_view()


shop_detail = DetailView.as_view(
    model = Shop,
)


class ShopCreateView(LoginRequiredMixin, CreateView):
    model = Shop
    form_class = ShopForm


shop_new = ShopCreateView.as_view()


class ShopUpdateView(LoginRequiredMixin, ShopUserCheckMixin, UpdateView):
    model = Shop
    form_class = ShopForm

    def get_success_url(self) -> str:
        post = self.object
        return resolve_url(post.shop)


shop_edit = ShopUpdateView.as_view()


class ShopDeleteView(LoginRequiredMixin, ShopUserCheckMixin, DeleteView):
    model = Shop
    form_class = DeleteForm

    def get_success_url(self) -> str:
        delete = self.object
        delete.save()
        return resolve_url(ShopListView)


shop_delete = DeleteView.as_view(
    model = Shop,
    success_url=reverse_lazy("shop:shop_list"),
)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    # # TODO: shop detail로 이동
    # success_url = reverse_lazy("shop:shop_list")

    # 유효성 검사에 통과한 후에 호출 ...
    def form_valid(self, form) -> HttpResponse:
        # self.kwargs : URL Captured 값들이 사전으로 저장
        shop_pk = self.kwargs["shop_pk"]
        shop = get_object_or_404(Shop, pk=shop_pk)

        review = form.save(commit=False)
        review.shop = shop
        review.user = self.request.user
        review.save()

        # return redirect("shop:shop_detail", shop.pk)
        return redirect(shop)


review_new = ReviewCreateView.as_view()


class ReviewUpdateView(LoginRequiredMixin, ReviewUserCheckMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    # FIXME: shop detail로 보내기
    # success_url = reverse_lazy("shop:shop_list")

    def get_success_url(self) -> str:
        review = self.object
        return resolve_url(review.shop)


review_edit = ReviewUpdateView.as_view()


review_delete = DeleteView.as_view(
    model = Shop,
    success_url=reverse_lazy("shop:shop_list"),
)