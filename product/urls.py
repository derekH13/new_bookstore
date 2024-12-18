from os.path import basename

from django.urls import path, include
from rest_framework import routers

from product import viewsets

# criando as rotas
router = routers.SimpleRouter()
# registrando as rotas e as viewsets
router.register(r'product', viewsets.ProductViewSet, basename='product')
router.register(r'category', viewsets.CategoryViewSet, basename='category')

urlpatterns = [
    path("", include(router.urls)),
]
