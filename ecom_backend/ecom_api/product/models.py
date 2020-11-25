from django.db import models
from ecom_api.category.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=250, null=True)
    price = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True, null=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name if self.name else ''
