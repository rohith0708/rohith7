from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart,Caarrt_item
from ecomapp.models import product
from django.core.exceptions import ObjectDoesNotExist


# Create your views here

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, Product_id):
    Product = product.objects.get(id=Product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save(),
    try:
        cart_item = Caarrt_item.objects.get(Product=Product, cart=cart)
        if cart_item.quantity < cart_item.Product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except Caarrt_item.DoesNotExist:
        cart_item = Caarrt_item.objects.create(
            Product=Product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = Caarrt_item.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.Product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, counter=counter, total=total))


def cart_remove(request,Product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    Product=get_object_or_404(product,id=Product_id)
    cart_item=Caarrt_item.objects.get(Product=Product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

def cart_delete(request,Product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    Product=get_object_or_404(product,id=Product_id)
    cart_item=Caarrt_item.objects.get(Product=Product,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')