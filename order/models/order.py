# importando uma estrutura user padrão
from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    # cada instancia de order pode ser associada a varios produtos
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
