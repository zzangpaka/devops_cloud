from django.contrib import admin

from book_report.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["book_name", "genre", "author_name", "created_at", "updated_at"]
    search_fields = ["genre"]
    search_fields2 = ["book_name"]
    search_fields3 = ["author_name"]



admin.site.register(Post, PostAdmin)
