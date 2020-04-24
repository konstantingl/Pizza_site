from django.urls import path
from . import views
from carts import views as v

urlpatterns = [
    path("", views.index, name="index"),
    path('cart/', v.cart_view, name='cart'),
    path('cart/<id>', v.update_cart, name='update_cart'),
]
