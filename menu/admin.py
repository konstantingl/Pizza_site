from django.contrib import admin

from menu.models import product, topping, subs_extra

admin.site.register(product)
admin.site.register(topping)
admin.site.register(subs_extra)
