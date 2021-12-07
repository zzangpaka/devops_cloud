from django.contrib import admin
from book.models import Profile, Book, Comment, Tag

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["title", "updated_at"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "genre", "title", "author", "updated_at"]
    list_display_links = ["title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["message", "name", "updated_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "updated_at"]