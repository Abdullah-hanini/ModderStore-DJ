from django.shortcuts import render ,get_object_or_404 , redirect
from django.core.paginator import Paginator
from .models import Products
from .filters import GamesFilter
from django.views.decorators.http import require_POST



def products_list(request):
    products_list = Products.objects.all()

    myfilter = GamesFilter(request.GET,queryset=products_list)
    products_list = myfilter.qs

    paginator = Paginator(products_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'games':page_obj ,'myfilter':myfilter}


    return render(request,'products/products_list.html',context)

def product_page(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context = {'game': product}
    return render(request, 'products/product_page.html', context)


def cart_page(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Products, id=product_id)
        total += product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity})
    context = {'cart_items': cart_items, 'total': total}
    return render(request, 'products/cart_page.html', context)


@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))

    if product_id:
        product = Products.objects.get(pk=product_id)
        cart = request.session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + quantity
        request.session['cart'] = cart

    return redirect('products:product_list')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    a = int (product_id)
    if product_id in cart:

        del cart [a]
        request.session['cart'] = cart
    return redirect('products:cart_page')

def update_cart(request, product_id):
    quantity = request.POST.get('quantity')
    cart = request.session.get('cart', {})
    if product_id in cart and quantity > 0:
        cart[product_id] = int(quantity)
        request.session['cart'] = cart
    return redirect('cart')
    

def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Products, id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })
        total += product.price * quantity
    order = Order.objects.create(total=total)
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
            subtotal=item['subtotal']
        )
    del request.session['cart']
    return render(request, 'products/checkout.html', {'order': order})