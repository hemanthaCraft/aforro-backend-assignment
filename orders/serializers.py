from rest_framework import serializers
from .models import Order


class OrderListSerializer(serializers.ModelSerializer):

    total_items = serializers.SerializerMethodField()

    class Meta:
        model = Order

        fields = [
            "id",
            "status",
            "created_at",
            "total_items"
        ]

    def get_total_items(self, obj):
        return obj.items.count()


class OrderItemInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity_requested = serializers.IntegerField()


class OrderCreateSerializer(serializers.Serializer):
    store_id = serializers.IntegerField()
    items = OrderItemInputSerializer(many=True)