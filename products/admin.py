from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product) # need to add product model so that we can add products to the site