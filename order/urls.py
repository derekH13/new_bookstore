from django.urls import path, include
from rest_framework import routers

from order import viewsets

# criando as rotas
router = routers.SimpleRouter()
# registrando as rotas e as viewsets
router.register(r"order", viewsets.OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
