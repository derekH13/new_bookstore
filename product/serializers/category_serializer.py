from rest_framework import serializers

from product.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # definindo o models como category, ja herda toda a estrurura
        model = Category
        # campos que eu quero exibir
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]
        extra_kwargs = {"slug": {"required": False}}
