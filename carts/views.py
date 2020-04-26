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
        print(total)
    the_cart.total = total

    context = {'cart': the_cart}
    return render(request, 'carts/cart.html', context)

def update_cart(request, id):
    cart_owner = Profile.objects.get(user=request.user)
    the_cart, created = cart.objects.get_or_create(owner=cart_owner)
    try:
        item = product.objects.get(id=id)
    except DoesNotExist:
        pass
    cart_obj, created = cart_item.objects.get_or_create(product=item, cart_one=the_cart)

    select = request.GET.get('size_select')
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
