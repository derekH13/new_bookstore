from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer

# estamos usando o ModelViewSet para sobreescrever ele


class CategoryViewSet(ModelViewSet):
    # definindo o serializer dessa viewset
    serializer_class = CategorySerializer

    # fazendo um queryset
    def get_queryset(self):
        # para definir a ordenação pelo id
        return Category.objects.all().order_by("id")
