from rest_framework import serializers

from product.models import Product, Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Product
        # campos que eu quero exibir
        fields = [
            "id",
            "title",
            "price",
            "active",
            "category_id",
            "category",
            "description",
        ]

    # sobre escrevendo uma função padrão do ModelSerializer
    def create(self, validated_data):
        # remove o campo categoria_id do dicionario
        category_data = validated_data.pop("category_id")

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)

        return product
