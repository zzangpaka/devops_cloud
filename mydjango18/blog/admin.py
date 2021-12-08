from django.contrib import admin

from blog.models import Profile, Post, Comment, Tag


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["title", "updated_at"]
    list_display_links = ["title"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "updated_at"]
    list_display_links = ["title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "updated_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]