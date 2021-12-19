from django.contrib import admin

from shop.models import Category, Shop, Tag, Review


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

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["shop", "title", "user"]
    list_display_links = ["title"]