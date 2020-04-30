from django.db import models
from menu.models import product
from account.models import Profile


# Create your models here.
class cart_item(models.Model):
    cart_one = models.ForeignKey('cart', on_delete=models.PROTECT,null=True, blank=True)
    product = models.ForeignKey(product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2, default = 0.00)
    line_total = models.DecimalField(max_digits=20, decimal_places=2, default = 0.00)
    notes = models.CharField(max_length = 128, null=True, blank=True)
    size = models.CharField(max_length = 5, null=True, blank=True)


    def __str__(self):
        return f"{self.product} {self.price}"

class cart(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(cart_item, null=True, blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, default = 0.00)

    def __str__(self):
        return str(self.id)
