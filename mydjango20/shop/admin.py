from django.contrib import admin
from shop.models import Shop, Review, Tag, Menu


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "telephone"]
    list_display_links = ["name"]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

