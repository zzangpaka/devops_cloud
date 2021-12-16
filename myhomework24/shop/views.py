from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from shop.forms import ShopForm
from shop.models import Shop

shop_list = ListView.as_view(
    model = Shop,
)


shop_detail = DetailView.as_view(
    model = Shop,
)


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm


shop_new = ShopCreateView.as_view()


class ShopUpdateView(UpdateView):
    model = Shop,
    form_class = ShopForm


shop_edit = ShopUpdateView.as_view()


shop_delete = DeleteView.as_view(
    model = Shop,
    success_url=reverse_lazy("shop:shop_list"),
)


# resell_list
#
#
# resell_detail
#
#
# resell_new
#
#
# resell_edit
#
#
# resell_delete