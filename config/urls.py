from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),

    path(
        "orders/",
        include("orders.urls")
    ),

    path(
        "stores/",
        include("stores.urls")
    ),

    path(
        "api/search/",
        include("search.urls")
    ),
]