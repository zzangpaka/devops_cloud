from django.urls import path

from shop import views


app_name = "shop"


urlpatterns = [
    path('', views.shop_list, name="shop_list"),
    path('detail/<int:pk>', views.shop_detail, name="shop_detail"),
    path('new/', views.shop_new, name="shop_new"),
    path('delete/<int:pk>', views.shop_delete, name="shop_delete"),
]