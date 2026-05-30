from django.urls import path

from .views import OrderCreateAPIView
from .views import StoreOrdersAPIView

urlpatterns = [

    path(
        "",
        OrderCreateAPIView.as_view(),
        name="create-order"
    ),

    path(
        "store/<int:store_id>/",
        StoreOrdersAPIView.as_view(),
        name="store-orders"
    ),
]