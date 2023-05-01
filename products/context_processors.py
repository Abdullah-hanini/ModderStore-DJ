from .models import Products

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = Products.objects.get(id=product_id)
        total += product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity})
    return {'cart': cart_items, 'total': total}
