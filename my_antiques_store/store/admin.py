from django.contrib import admin
from .models import Product, Owner


admin.site.register(Owner)
admin.site.register(Product)

