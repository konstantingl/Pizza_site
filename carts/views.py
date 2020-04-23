from django.shortcuts import render, redirect
from menu.models import product, topping, subs_extra
from carts.models import cart
# Create your views here.

def cart_view(request):
    the_cart = cart.objects.all()[0]
    context = {'cart': the_cart}
    return render(request, 'carts/cart.html', context)

def update_cart(request, id):
    the_cart = cart.objects.all()[0]
    try:
        item = product.objects.get(id=id)
    except product.DoesNotExist:
        pass
    the_cart.products.add(item)
    return redirect('cart')
