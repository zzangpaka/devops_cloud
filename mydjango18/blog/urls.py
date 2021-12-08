from django.urls import path

from blog import views


app_name = 'blog'


urlpatterns = [
    path("", views.profile, name="profile"),
    path("post_list/", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
]
