from django.db import models
from menu.models import product

# Create your models here.
class cart(models.Model):
    products = models.ManyToManyField(product, null=True, blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, default = 0.00)

    def __unicode__(self):
        return str(self.id)
