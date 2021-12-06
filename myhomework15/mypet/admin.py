from django.contrib import admin

from mypet.models import Pet


class MyPet(admin.ModelAdmin):
    list_display = ["id", "title", "name", "created_at"]
    list_display_links = ["title"]

admin.site.register(Pet, MyPet)