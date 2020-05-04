from django.shortcuts import render, redirect
from menu.models import product, topping, subs_extra
from carts.models import cart, cart_item
from account.models import Profile
from django.http import HttpResponse
from django.db.models.base import ObjectDoesNotExist
from decimal import *

# Open cart
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


# Add items to cart
def update_cart(request):
    cart_owner = Profile.objects.get(user=request.user)
    the_cart, created = cart.objects.get_or_create(owner=cart_owner)

    # Data processing from http request with item to add from user
    data = request.POST.copy()
    name = data.get('product_selected')
    print(name)
    tops = data.get('tops_selected')
    size = data.get('size')
    extras_names = data.get('extra_selected')

    if not extras_names: extras_amount = 0
    else: extras_amount = len(extras_names.split(','))

    if tops: notes = tops
    elif extras_names: notes = extras_names
    else: notes = None

    # Create a cart item with details about size, price, notes
    try:
        item = product.objects.get(name=name)
        print(item)
    except ObjectDoesNotExist:
        HttpResponse("Error!")

    cart_obj, created = cart_item.objects.get_or_create(product=item, cart_one=the_cart, size=size, notes=notes)

    if size == 'small':
        cart_obj.price = item.small_price + Decimal(0.5*extras_amount)
        cart_obj.save()
    elif size == 'large':
        cart_obj.price = item.large_price + Decimal(0.5*extras_amount)
        cart_obj.save()
    else:
        HttpResponse("Error!")

    the_cart.products.add(cart_obj)

    return redirect("cart")

# Remove item from cart
def remove_from_cart(request, id):
    cart_owner = Profile.objects.get(user=request.user)
    the_cart = cart.objects.get(owner=cart_owner)
    cart_obj = cart_item.objects.get(id=id, cart_one=the_cart)
    the_cart.products.remove(cart_obj)
    return redirect("cart")
