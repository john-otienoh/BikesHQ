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
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="shop/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("account:profile", args=[self.id])
