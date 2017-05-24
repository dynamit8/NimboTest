from django.contrib import admin

# Register your models here.

from .models import product
admin.site.register(product)

from .models import order
admin.site.register(order)

from .models import productListedInOrder
admin.site.register(productListedInOrder)