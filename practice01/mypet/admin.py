from django.contrib import admin
from mypet.models import Pet


class MyPet(admin.ModelAdmin):
    list_display = ["id", "name", "description", "created_at"]
    list_display_links = ["name"]

admin.site.register(Pet, MyPet)