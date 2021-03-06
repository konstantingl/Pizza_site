from django.db import models

class product(models.Model):
    category = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.name} from {self.category}"

class topping(models.Model):
    topping_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping_name}"

class subs_extra(models.Model):
    extra_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.extra_name}"
