from django.contrib import admin
from .models import Product, Category, Brand, Slide, CartItem, Order, OrderProduct


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'category', 'brand', 'price']
    search_fields = ['title', 'description']
    list_filter = ['category', 'brand', 'price']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'quantity']


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Slide)
admin.site.register(Order)
admin.site.register(OrderProduct)
