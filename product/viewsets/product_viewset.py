from rest_framework.viewsets import ModelViewSet


from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        # para definir a ordenação pelo id
        return Product.objects.all().order_by("id")
