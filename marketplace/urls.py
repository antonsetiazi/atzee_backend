# marketplace/urls.py

from django.urls import path
from marketplace.views.order_views import (
    CreateOrderView,
    OrderListView,
    OrderDetailView,
)

urlpatterns = [
    path("orders/", OrderListView.as_view()),        # GET list
    path("orders/create/", CreateOrderView.as_view()),  # POST create (optional pisah)
    path("orders/<int:id>/", OrderDetailView.as_view()),
]