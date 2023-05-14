
from django.urls import include, path

from . import views
app_name = 'products'

urlpatterns = [
    path('', views.products_list,name='product_list'),
    path('<str:slug>', views.product_page),
    path('cart/', views.cart_page, name='cart_page'),
    path('search/', views.search, name='search'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart_i/<int:product_id>/', views.aupdate_cart, name='update_cart_i'),
    path('update_cart_d/<int:product_id>/', views.bupdate_cart, name='update_cart_d'),
    path('order/<int:order_id>/', views.order_d, name='order'),
    path('checkout/', views.checkout, name='checkout'),
    path('sendm/', views.sendm, name='sendm'),


]
