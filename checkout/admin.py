from django.contrib import admin
from checkout.models import BillingDetail, Checkout

# Register your models here.

class BillingDetailAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_added'
    search_fields = ['username', 'first_name', 'last_name']
    list_display = ['user', 'date_added']
    readonly_fields = ['user','first_name','last_name','company_name','country','district','city','street','zip_code','phone','email','order_notes','payment_method','date_added']
    class Meta:
        model = BillingDetail

class CheckoutAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_added'
    search_fields = ['user', 'status']
    readonly_fields = ['user', 'cart', 'checkout_id', 'date_added']
    class Meta:
        model = Checkout

admin.site.register(BillingDetail, BillingDetailAdmin)
admin.site.register(Checkout, CheckoutAdmin)
