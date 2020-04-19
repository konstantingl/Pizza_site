from django.db import models

class regular_pizza(models.Model):
    pizza_name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.pizza_name} {self.small_price} {self.large_price}"

class sicilian_pizza(models.Model):
    pizza_name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

class toppings(models.Model):
    topping_name = models.CharField(max_length=64)

class subs(models.Model):
    sub_name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

class subs_extras(models.Model):
    extra_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

class pastas(models.Model):
    pasta_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

class salads(models.Model):
    salad_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

class dinner_platters(models.Model):
    dinner_name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
