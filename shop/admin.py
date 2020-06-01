from django.contrib import admin
from shop.models import Product, Contact, Sell

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_added'
    search_fields = ['title', 'description']
    list_display = ['title', 'new_price', 'available_in_stock']
    list_editable = ['new_price', 'available_in_stock']
    list_filter = ['new_price', 'available_in_stock']
    readonly_fields = ['date_added', 'date_updated']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

admin.site.register(Contact)

admin.site.register(Sell)
