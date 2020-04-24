from django.shortcuts import render, redirect
from menu.models import product, topping, subs_extra
from carts.models import cart, cart_item
from django.http import HttpResponse
# Create your views here.

def cart_view(request):
    the_cart = cart.objects.all()[0]
    context = {'cart': the_cart}
    return render(request, 'carts/cart.html', context)

def update_cart(request, id):
    select = request.GET.get('size_select')
    the_cart = cart.objects.all()[0]
    try:
        item = product.objects.get(id=id)
    except DoesNotExist:
        pass
    cart_obj, created = cart_item.objects.get_or_create(product=item, cart_one=the_cart)

    if select == 'small':
        cart_obj.price = item.small_price
        cart_obj.save()
    elif select == 'large':
        cart_obj.price = item.large_price
        cart_obj.save()
    else:
        HttpResponse("Error!")

    the_cart.products.add(cart_obj)

    return redirect("cart")
