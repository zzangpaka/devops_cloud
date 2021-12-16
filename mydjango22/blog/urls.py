from django.urls import path

from blog import views


app_name = 'blog'


urlpatterns = [
    path('', views.hello, name="hello"),
    path('post/list/', views.post_list, name="post_list"),
    path('post/detail/<int:pk>/', views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name="post_new"),
    path('post/edit/<int:pk>/', views.post_edit, name="post_edit"),
    path('post/delete/<int:pk>/', views.post_delete, name="post_delete"),
    path('review/list/', views.review_list, name="review_list"),
    path('review/detail/<int:pk>/', views.review_detail, name="review_detail"),
    path('review/new/', views.review_new, name="review_new"),
    path('review/edit/<int:pk>/', views.review_edit, name="review_edit"),
    path('review/delete/<int:pk>/', views.review_delete, name="review_delete"),
]
