from django.contrib import admin
from shop.models import Category, Shop, Review, Tag, Menu


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "telephone"]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["author_name", "message"]
    list_display_links = ["message"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]

