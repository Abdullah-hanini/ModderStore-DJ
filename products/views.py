from django.shortcuts import render ,get_object_or_404 , redirect
from django.core.paginator import Paginator
from .models import Products , Orders , OrderItem , Category
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from .filters import GamesFilter
from django.views.decorators.http import require_POST
from .forms import ProfileForm
import datetime


def products_list(request, category=None):
    products_list = Products.objects.filter(is_hidden=False)

    if category is not None:
        category_obj = get_object_or_404(Category, name=category)
        products_list = products_list.filter(category=category_obj)

    myfilter = GamesFilter(request.GET, queryset=products_list)
    products_list = myfilter.qs

    paginator = Paginator(products_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'games': page_obj, 'myfilter': myfilter, 'category': category}

    return render(request, 'products/products_list.html', context)



def search(request, category=None):
    products_list = Products.objects.all()
    if category is not None:
        category_obj = get_object_or_404(Category, name=category)
        products_list = products_list.filter(category=category_obj)

    myfilter = GamesFilter(request.GET, queryset=products_list)
    products_list = myfilter.qs

    paginator = Paginator(products_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'games': page_obj, 'myfilter': myfilter, 'category': category}

    return render(request, 'products/products_list.html', context)
    
def product_page(request, slug):
    product = get_object_or_404(Products, slug=slug)
    products_list = Products.objects.filter(is_hidden=False,is_ent=False)
    hidden_related_products = product.related_products.filter()
    paginator = Paginator(products_list, 4)
    rgames = paginator.get_page(1)
    context = {'game': product,'hgame':hidden_related_products ,'games':rgames}
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

    return redirect('products:cart_page')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    a = str(product_id)
    if a in cart:
        del cart[a]
        request.session['cart'] = cart
    return redirect('products:cart_page')


def aupdate_cart(request, product_id):
    cart = request.session.get('cart', {})
    a = str(product_id)
    if a in cart:
        cart[a] += 1
        request.session['cart'] = cart
    return redirect('products:cart_page')

def bupdate_cart(request, product_id):
    cart = request.session.get('cart', {})
    a = str(product_id)
    if a in cart:
        if cart[a] > 1:
            cart[a] -= 1
        else:
            del cart[a]
        request.session['cart'] = cart
    return redirect('products:cart_page')

@login_required
def place_the_order(request):
    cart = request.session.get('cart', {})
    products = Products.objects.filter(id__in=cart.keys())
    total = 0
    user_profile = Profile.objects.get(user=request.user)

    for product in products:
        quantity = cart[str(product.id)]
        total += product.price * quantity
    order = Orders.objects.create(user=request.user, total=total ,email = user_profile.user.email ,phonen=user_profile.phonenumber ,pdiscrption='Order placed through website.',alias=user_profile.cliq)
    for product in products:
        quantity = cart[str(product.id)]
        OrderItem.objects.create(order=order, product=product, quantity=quantity)
        
    request.session['cart'] = {}
    return redirect('products:order', order_id=order.id)


@login_required
def sendm (request):
    cart = request.session.get('cart', {})
    products = Products.objects.filter(id__in=cart.keys())
    total = 0
    if cart == {}: 
        return redirect('products:product_list')
    else:
        for product in products:
            quantity = cart[str(product.id)]
            total += product.price * quantity
        context = {'total': total}    
        
        return render(request, 'products/sendm.html', context)
    
    
@login_required
def checkout (request):
    cart = request.session.get('cart', {})
    profile = Profile.objects.get(user=request.user)
    if cart == {}:
        return redirect('products:product_list')
    else:
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
                return sendm(request)
        else: 
            profile_form = ProfileForm(instance=profile)
            
        if request.method == 'GET' and 'send_data' in request.GET:
            return place_the_order(request)   
    return render(request,'products/checkout_page.html',{'profile_form':profile_form})


@login_required
def order_d (request, order_id):
    order = get_object_or_404(Orders, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    context = {'order': order, 'order_items': order_items}
    if request.user.is_superuser:
        return render(request, 'products/order.html', context)
    elif (request.user==order.user):
        return render(request, 'products/order.html', context)
    else :
        return redirect('products:product_list')
