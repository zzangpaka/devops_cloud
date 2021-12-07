from blog import views
from django.urls import path


app_name = "blog"


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post.detail"),
    path("tags/<str:tag_name>/", views.tag_detail, name="tag_detail"),
]