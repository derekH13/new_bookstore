from django.db import models

from product.models import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    # defini que muitos produtos podem ter diversas categorias
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title