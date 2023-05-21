from .models import Products
from .serializers import productsSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def product_list(request):
    all_products = Products.objects.all()
    data = productsSerializer(all_products, many=True).data
    return Response({'data': data})