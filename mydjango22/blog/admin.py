from django.contrib import admin

from blog.models import Post, Review, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["category", "title", "author_name", "updated_at"]
    list_display_links = ["title"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["post", "title", "author_name", "updated_at"]
    list_display_links = ["title"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]