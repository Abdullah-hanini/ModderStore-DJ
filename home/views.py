from django.shortcuts import render
from .models import hot_pro , entertainment
from products.models import Products

def home(request):
    Hot_pro = hot_pro.objects.first()
    ent = entertainment.objects.first()
    products_hot = Hot_pro.product.all()
    products_ent = ent.product.all()
    context = {'games': products_hot, 'ent': products_ent}
    return render(request, 'home/home.html', context)
