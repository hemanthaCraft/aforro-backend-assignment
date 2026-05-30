from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product

from .serializers import ProductSearchSerializer
from .pagination import ProductPagination

from products.models import Product


class ProductSearchAPIView(APIView):

    def get(self, request):

        queryset = Product.objects.select_related(
            "category"
        ).order_by("id").distinct()

        keyword = request.GET.get("q")

        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword)
                |
                Q(description__icontains=keyword)
                |
                Q(category__name__icontains=keyword)
            )

        category = request.GET.get(
            "category"
        )

        if category:
            queryset = queryset.filter(
                category__name__iexact=category
            )

        min_price = request.GET.get(
            "min_price"
        )

        max_price = request.GET.get(
            "max_price"
        )

        if min_price:
            queryset = queryset.filter(
                price__gte=min_price
            )

        if max_price:
            queryset = queryset.filter(
                price__lte=max_price
            )
            
        # Store Filter

        store = request.GET.get("store")

        if store:
            queryset = queryset.filter(
                inventories__store_id=store
            ).distinct()

        


        # In Stock Filter

        in_stock = request.GET.get(
            "in_stock"
        )

        if in_stock == "true":
            queryset = queryset.filter(
                inventories__quantity__gt=0
            ).distinct()


        # Sorting

        sort = request.GET.get("sort")

        if sort in [
            "price",
            "-price",
            "title",
            "-title"
        ]:
            queryset = queryset.order_by(
                sort
            )

        paginator = ProductPagination()

        page = paginator.paginate_queryset(
            queryset,
            request
        )

        serializer = ProductSearchSerializer(
            page,
            many=True
        )

        return paginator.get_paginated_response(
            serializer.data
        )
        
class ProductSuggestAPIView(APIView):

    def get(self, request):

        q = request.GET.get("q", "")

        if len(q) < 3:
            return Response(
                {
                    "error":
                    "Minimum 3 characters required"
                },
                status=400
            )

        suggestions = list(

            Product.objects.filter(
                title__istartswith=q
            )
            .values_list(
                "title",
                flat=True
            )[:10]

        )

        return Response(
            suggestions
        )