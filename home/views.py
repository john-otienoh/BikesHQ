from django.shortcuts import render
from shop.models import Product
from category.models import Category
from django.db.models import Count

# Create your views here.


def home(request):
    # products = Product.objects.filter(is_available=True)

    products = (
        Product.objects.filter(is_available=True)
        .annotate(rand_id=Count("id"))
        .order_by("rand_id")[:4]
    )
    parent_categories = Category.objects.filter(parent__isnull=True)
    return render(
        request,
        "home/index.html",
        {"products": products, "parent_categories": parent_categories},
    )
