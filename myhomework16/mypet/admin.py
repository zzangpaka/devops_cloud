from django.contrib import admin

from mypet.models import MyPet



class MyPetAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "title", "created_at"]
    list_display_links = ["title"]

admin.site.register(MyPet, MyPetAdmin)