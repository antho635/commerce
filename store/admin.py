from django.contrib import admin
from store.models import Product, Order, Cart, Category

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
