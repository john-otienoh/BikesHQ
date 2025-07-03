from django.db import models
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(
        max_length=250,
        unique=True,
    )
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="category/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        # indexes = [
        #     models.Index(fields=['-publish']),
        # ]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_by_category", args=[self.slug])

    def is_main_category(self):
        return self.parent is None

    def is_subcategory(self):
        return self.parent and self.parent.is_main_category()

    def get_icon_class(self):
        if self.icon:
            return self.icon
        # Default icons for main categories
        if self.name == "Bikes":
            return "bi bi-bicycle"
        elif self.name == "Parts & Upgrades":
            return "bi bi-tools"
        elif self.name == "Bike Accesories":
            return "bi bi-gear-wide"
        return "bi bi-bag"
