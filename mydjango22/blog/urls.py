from django.urls import path

from blog import views


app_name = 'blog'


urlpatterns = [
    path('', views.hello, name="hello"),
    path('list/', views.post_list, name="post_list"),
    path('detail/<int:pk>/', views.post_detail, name="post_detail"),
]