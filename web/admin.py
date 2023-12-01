# admin.py

from django.contrib import admin
from .models import Product, Stock

class StockInline(admin.StackedInline):
    model = Stock
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [StockInline]
    list_display = ['name', 'price']
    search_fields = ['name']

class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'location', 'last_updated']
    list_filter = ['location']
    search_fields = ['product__name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
