from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from shop.models import Product

# Create your views here.

@login_required
def cart(request):
    try:
        new_id = request.session['cart_id']
    except:
        new_id =None
    if new_id:
        cart = Cart.objects.get(id=new_id)
        context = {'carts':cart}
    else:
        message = "Your cart is empty."
        context = {'empty':True, 'message': message}
    return render(request, 'cart-page.html', context)

def update_cart(request, product_code):
    request.session.set_expiry(2592000)           #the cart will cleared after this time or when the user logs out
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        new_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        new_id = new_cart.id

    cart = Cart.objects.get(id=new_id)
    try:
        product = Product.objects.get(product_code=product_code)
    except Product.DoesNotExist:
        pass
    except:
        pass
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        print('hello buddy')

    if qty and update_qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass

    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)

    new_sub_total = 0.00
    new_tax = 0.00
    new_shipping = 0.00
    new_total = 0.00
    tax_rate = 0.13
    shipping_rate = 0.1
    for item in cart.cartitem_set.all():
        each_total = float(item.product.new_price) * item.quantity
        new_sub_total += each_total
        new_tax = new_sub_total * tax_rate
        new_shipping = new_sub_total * shipping_rate
        new_total = new_sub_total + new_tax + new_shipping
    request.session['items_total'] = cart.cartitem_set.count()    #returns the no of items to navbar cart
    cart.sub_total = new_sub_total
    cart.tax = new_tax
    cart.shipping = new_shipping
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse('cart'))
