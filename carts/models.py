from django.db import models
from menu.models import product

# Create your models here.
class cart_item(models.Model):
    cart_one = models.ForeignKey('cart', on_delete=models.PROTECT)
    product = models.ForeignKey(product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2, default = 0.00)
    line_total = models.DecimalField(max_digits=20, decimal_places=2, default = 0.00)

    def __str__(self):
        return f"{self.product} {self.price}"

class cart(models.Model):
    products = models.ManyToManyField(cart_item, null=True, blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, default = 0.00)

    def __str__(self):
        return str(self.id)
