from rest_framework import serializers
from products.models import Product


class ProductSearchSerializer(serializers.ModelSerializer):

    category = serializers.CharField(
        source="category.name"
    )

    class Meta:
        model = Product

        fields = [
            "id",
            "title",
            "description",
            "price",
            "category"
        ]