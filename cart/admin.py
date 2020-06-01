from django.contrib import admin
from cart.models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    readonly_fields = ['date_added', 'date_updated']
    class Meta:
        model = Cart

admin.site.register(Cart, CartAdmin)

admin.site.register(CartItem)
