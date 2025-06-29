from django.shortcuts import render
from .models import Product


# Create your views here.
def store(request):
    products = Product.objects.filter(is_available=True)
    return render(request, "home/index.html", {"products": products})
