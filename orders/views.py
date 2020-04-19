from django.http import HttpResponse
from django.shortcuts import render
from orders.models import regular_pizza, sicilian_pizza, toppings, subs, subs_extras, pastas, salads, dinner_platters

# Create your views here.
def index(request):
    context = {
    "regular_pizza": regular_pizza.objects.all(),
    "sicilian_pizza": sicilian_pizza.objects.all(),
    "toppings": toppings.objects.all(),
    "subs": subs.objects.all(),
    "subs_extras": subs_extras.objects.all(),
    "pastas": pastas.objects.all(),
    "salads": salads.objects.all(),
    "dinner_platters": dinner_platters.objects.all(),
    }
    return render(request, 'orders/index.html', context)
