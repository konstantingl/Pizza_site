from django.shortcuts import render, redirect
from menu.models import product, topping, subs_extra
from carts.models import cart, cart_item
from account.models import Profile
from django.http import HttpResponse
# Create your views here.

def cart_view(request):
    cart_owner = Profile.objects.get(user=request.user)
    the_cart, created = cart.objects.get_or_create(owner=cart_owner)

    # Cart total count
    total = 0
    for i in the_cart.products.all():
        print (i.price)
        total += i.price
    the_cart.total = total

    context = {'cart': the_cart}
    return render(request, 'carts/cart.html', context)

def update_cart(request):
    cart_owner = Profile.objects.get(user=request.user)
    the_cart, created = cart.objects.get_or_create(owner=cart_owner)

    data = request.POST.copy()
    name = data.get('product_selected')
    tops = data.get('tops_selected')
    size = data.get('size')

    try:
        item = product.objects.get(name=name)
    except DoesNotExist:
        pass
    cart_obj, created = cart_item.objects.get_or_create(product=item, cart_one=the_cart, size=size, notes=tops)

    if size == 'small':
        cart_obj.price = item.small_price
        cart_obj.save()
    elif size == 'large':
        cart_obj.price = item.large_price
        cart_obj.save()
    else:
        HttpResponse("Error!")

    the_cart.products.add(cart_obj)

    return redirect("cart")
