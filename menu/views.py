from django.http import HttpResponse
from django.shortcuts import render, redirect
from menu.models import product, topping, subs_extra

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {
        "regular_pizza": product.objects.filter(category='Regular Pizza'),
        "sicilian_pizza": product.objects.filter(category='Sicilian Pizza'),
        "subs": product.objects.filter(category='Sub'),
        "pastas": product.objects.filter(category='Pasta'),
        "salads": product.objects.filter(category='Salad'),
        "dinners": product.objects.filter(category='Dinner'),
        "toppings": topping.objects.all(),
        "subs_extras": subs_extra.objects.all(),
        }
        return render(request, 'orders/index.html', context)

    else:
        return redirect('login')
