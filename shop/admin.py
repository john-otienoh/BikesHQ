from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "slug",
        "image",
        "is_available",
        "category",
        "price",
        "stock",
    ]
    list_filter = ["name", "is_available", "category"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ["category"]
    date_hierarchy = "updated_at"
    ordering = ["updated_at", "price"]
    show_facets = admin.ShowFacets.ALWAYS
