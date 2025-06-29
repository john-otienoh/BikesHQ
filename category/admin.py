from django.contrib import admin
from .models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "slug",
        "image",
        "created_at",
        "updated_at",
        "parent",
    ]
    list_filter = ["created_at", "parent"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    # raw_id_fields = ['author']
    date_hierarchy = "updated_at"
    ordering = ["updated_at"]
    show_facets = admin.ShowFacets.ALWAYS
