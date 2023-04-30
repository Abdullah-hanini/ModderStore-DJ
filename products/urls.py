
from django.urls import include, path

from . import views
app_name = 'product'

urlpatterns = [
    path('', views.products_list,name='product_list'),
    path('<str:slug>', views.product_page),
]
