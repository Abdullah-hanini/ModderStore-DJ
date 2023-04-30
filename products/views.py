from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products

def products_list(request):
    products_list = Products.objects.all()
    paginator = Paginator(products_list, 12)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'games':page_obj}


    return render(request,'products/products_list.html',context)

def product_page(request , slug):
    product_page = Products.objects.get(slug=slug)
    context = {'game':product_page}
    return render(request,'products/product_page.html',context)