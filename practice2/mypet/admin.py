from django.contrib import admin


from mypet.models import MyPet, Comment, Tag


@admin.register(MyPet)
class MyPetAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "title", "created_at"]
    list_display_links = ["title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["pk", "mypet", "message", "created_at"]
    list_display_links = ["mypet"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass