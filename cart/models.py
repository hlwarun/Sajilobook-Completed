from django.db import models
from shop.models import Product

# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    each_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Cart id: %s" %(self.cart.id)

class Cart(models.Model):
    #items = models.ManyToManyField(CartItem, blank=True)
    #products = models.ManyToManyField(Product, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    sub_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    shipping = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    tax = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    def __str__(self):
        return "Cart id: %s" %(self.id)
