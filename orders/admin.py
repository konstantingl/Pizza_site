from django.contrib import admin

from orders.models import regular_pizza, sicilian_pizza, toppings, subs, subs_extras, pastas, salads, dinner_platters

admin.site.register(regular_pizza)
admin.site.register(sicilian_pizza)
admin.site.register(toppings)
admin.site.register(subs)
admin.site.register(subs_extras)
admin.site.register(salads)
admin.site.register(dinner_platters)
