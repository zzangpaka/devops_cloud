from django.contrib import admin

from shop.forms import ShopForm
from shop.models import Category, Shop, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form = ShopForm

    list_display = ['id', 'name', 'telephone']
    list_display_links = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
