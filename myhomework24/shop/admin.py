from django.contrib import admin

from shop.models import Category, Shop, Tag, Resell


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["category", "title", "author_name"]
    list_display_links = ["title"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Resell)
class ResellAdmin(admin.ModelAdmin):
    list_display = ["category", "title", "user"]
    list_display_links = ["title"]