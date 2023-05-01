
from django.urls import include, path

from . import views
app_name = 'products'

urlpatterns = [
    path('', views.products_list,name='product_list'),
    path('<str:slug>', views.product_page),
    path('cart/', views.cart_page, name='cart_page'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
]
