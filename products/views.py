from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products
from .filters import GamesFilter



def products_list(request):
    products_list = Products.objects.all()

    myfilter = GamesFilter(request.GET,queryset=products_list)
    products_list = myfilter.qs

    paginator = Paginator(products_list, 12)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'games':page_obj ,'myfilter':myfilter}


    return render(request,'products/products_list.html',context)

def product_page(request , slug):
    product_page = Products.objects.get(slug=slug)
    context = {'game':product_page}
    return render(request,'products/product_page.html',context)