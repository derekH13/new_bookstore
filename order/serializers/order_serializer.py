from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    # many=True diz que pode ter mais de um produto para uma determinada ordem
    product = ProductSerializer(read_only=True, many=True)
    # isso é um lazy valuate, o django não carrega todos os dados ele só traz uma referencia
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )
    # SerializerMethodField basicamente dizendo que o valor vai vir de um metodo
    total = serializers.SerializerMethodField()

    # fazer a soma do total dos preços dos produtos do banco de dados
    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        # os campos que iram aparecer ao fazer request
        fields = ["product", "total", "product_id", "user"]
        model = Order
        # deixando o campo produto sem ser obragatorio
        extra_kwargs = {"product": {"required": False}}

    # sobre escrevendo uma função do ModelSerializer
    def create(self, validated_data):
        # tira todos os valores product_id
        product_data = validated_data.pop("product_id")
        # tira todos os valores user
        user_data = validated_data.pop("user")

        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)

        return order
