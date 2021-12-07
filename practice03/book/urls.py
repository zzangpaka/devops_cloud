from django.urls import path

from book import views


app_name = "book"


urlpatterns = [
    path("", views.profile, name="profile"),
    path("book/", views.book_list, name="book_list")
]
