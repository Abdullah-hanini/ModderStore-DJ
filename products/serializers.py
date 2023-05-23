from rest_framework import serializers

from .models import Products, Orders

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
class ordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'