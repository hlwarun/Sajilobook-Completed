from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from cart.models import Cart

# Create your models here.

User = get_user_model()

STATUS = (
    ('Shipped','Shipped'),
    ('Abandoned','Abandoned'),
    ('Delivered','Delivered'),
)

PAYMENT_CHOICES = (('Cash on delivery', 'Cash on delivery'),
                    ('Direct bank transfer', 'Direct bank transfer'),
                    ('Cheque payments', 'Cheque payments'),)

class Checkout(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    checkout_id = models.CharField(unique=True, max_length=100)
    status = models.CharField(max_length=50, default="Shipped", choices=STATUS)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Checkout id: %s" %(self.id)

class BillingDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    company_name = models.CharField(max_length=75, blank=True, null=True)
    country = models.CharField(choices=(('Nepal', 'Nepal'),), max_length=10, default='Nepal')
    district = models.CharField(max_length=25, blank=True, null=True)
    city = models.CharField(max_length=25)
    street = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    order_notes = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='Cash on delivery')
    date_added = date_added = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user.username)
