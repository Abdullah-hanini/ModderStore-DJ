from django.contrib import admin

# Register your models here.
from .models import Products , Category,Orders,OrderItem

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(OrderItem)
