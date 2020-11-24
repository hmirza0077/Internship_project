from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [

    path('', views.product_list, name='product_list'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/<int:id>/', views.wishlist, name='add_to_wishlist'),
    path('GET/', views.product_list, name='product_list'),
    path('wishlist/remove/<int:id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<str:gender>/', views.product_list, name='product_list_by_gender'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<int:id>/<slug:slug>/<str:color>/', views.product_detail, name='product_detail_by_color'),
]