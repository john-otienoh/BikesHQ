from django.db import models
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify
from category.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(
        max_length=250,
        unique=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    specs = models.JSONField(default=dict)
    image_url = models.URLField(max_length=500, blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="shop/", blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        limit_choices_to={"parent__isnull": False},
        related_name="products",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])
