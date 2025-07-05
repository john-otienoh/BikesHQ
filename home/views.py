from django.shortcuts import get_object_or_404, render
from shop.models import Product
from category.models import Category
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache

# Create your views here.


def home(request):
    # products = Product.objects.filter(is_available=True)

    random_products = (
        Product.objects.filter(is_available=True)
        .annotate(rand_id=Count("id"))
        .order_by("rand_id")[:4]
    )
    parent_categories = Category.objects.filter(parent__isnull=True)
    return render(
        request,
        "home/index.html",
        {"random_products": random_products, "parent_categories": parent_categories},
    )


def products(request, category_slug=None):

    categories = None
    product_list = None
    page_obj = 0
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        all_products = Product.objects.filter(category=categories, is_available=True)
        product_count = all_products.count()
        paginator = Paginator(all_products, 3)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        try:
            all_products = paginator.page(page_number)
        except EmptyPage:
            all_products = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            all_products = paginator.page(1)
    else:
        product_list = Product.objects.filter(is_available=True)
        product_count = product_list.count()
        paginator = Paginator(product_list, 3)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        try:
            all_products = paginator.page(page_number)
        except EmptyPage:
            all_products = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            all_products = paginator.page(1)
        
    return render(
        request,
        "home/products.html",
        {"all_products": all_products, 'product_count': product_count, 'page_obj': page_obj},
    )


def product_detail(request, product):
    product = get_object_or_404(Product, slug=product)
    return render(request, "home/product_detail.html", {"product": product})
