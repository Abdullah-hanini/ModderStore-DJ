from .models import Products, Orders
from .serializers import productsSerializer , ordersSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import *


@api_view(['GET'])
def product_list(request):
    all_products = Products.objects.all()
    data = productsSerializer(all_products, many=True).data
    return Response({'data': data})



class product_view(RetrieveUpdateDestroyAPIView):
    serializer_class = productsSerializer
    queryset = Products.objects.all()
    lookup_field='id'
    
    
class orders(RetrieveUpdateDestroyAPIView):
    serializer_class = ordersSerializer
    queryset = Orders.objects.all()


class orders_view(RetrieveUpdateDestroyAPIView):
    serializer_class = ordersSerializer
    queryset = Orders.objects.all()
    lookup_field='id'
    