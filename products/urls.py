
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.products_list),
    path('<str:slug>', views.product_page),
]
