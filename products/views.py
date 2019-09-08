from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all() # returns all products in database
    return render(request, "products.html", {"products": products})