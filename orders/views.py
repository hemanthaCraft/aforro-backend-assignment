from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OrderCreateSerializer

from stores.models import Store, Inventory
from products.models import Product
from .models import Order, OrderItem

from django.db.models import Prefetch
from .models import Order
from .serializers import OrderListSerializer

from .tasks import process_order


class OrderCreateAPIView(APIView):

    @transaction.atomic
    def post(self, request):

        serializer = OrderCreateSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        store_id = serializer.validated_data["store_id"]
        items = serializer.validated_data["items"]

        store = Store.objects.get(
            id=store_id
        )

        order = Order.objects.create(
            store=store,
            status=Order.PENDING
        )

        for item in items:

            inventory = Inventory.objects.filter(
                store=store,
                product_id=item["product_id"]
            ).first()

            if (
                not inventory
                or
                inventory.quantity <
                item["quantity_requested"]
            ):

                order.status = Order.REJECTED
                order.save()

                return Response({
                    "status": "REJECTED",
                    "order_id": order.id
                })

        for item in items:

            inventory = Inventory.objects.get(
                store=store,
                product_id=item["product_id"]
            )

            inventory.quantity -= item[
                "quantity_requested"
            ]

            inventory.save()

            product = Product.objects.get(
                id=item["product_id"]
            )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity_requested=item[
                    "quantity_requested"
                ]
            )

        order.status = Order.CONFIRMED
        order.save()
        
        process_order.delay(order.id)

        return Response({
            "status": "CONFIRMED",
            "order_id": order.id
        })

class StoreOrdersAPIView(APIView):

    def get(self, request, store_id):

        orders = (
            Order.objects
            .filter(
                store_id=store_id
            )
            .prefetch_related(
                "items"
            )
            .order_by(
                "-created_at"
            )
        )

        serializer = OrderListSerializer(
            orders,
            many=True
        )

        return Response(
            serializer.data
        )