# marketplace/urls.py

from django.urls import path
from marketplace.views.order_views import (
    OrderPreviewView,
    CreateOrderView,
    OrderListView,
    OrderDetailView,
    CompleteOrderView,
    AssignPartnerView,
    AcceptOrderView,
    RejectOrderView,
)

from marketplace.views.partner_order_views import (
    PartnerOrderDetailView,
    PartnerOrderListView
)
urlpatterns = [
    path("orders/", OrderListView.as_view()),        # GET list
    path("orders/create/", CreateOrderView.as_view()),  # POST create (optional pisah)
    path("orders/<int:id>/", OrderDetailView.as_view()),

    path("orders/<int:id>/complete/", CompleteOrderView.as_view()),
    path("orders/<int:id>/assign-partner/", AssignPartnerView.as_view()),
    path("orders/<int:id>/accept/", AcceptOrderView.as_view()),
    path("orders/<int:id>/reject/", RejectOrderView.as_view()),
    path("orders/preview/", OrderPreviewView.as_view()),

    path("partner/orders/", PartnerOrderListView.as_view()),
    path("partner/orders/<int:id>/", PartnerOrderDetailView.as_view()),
]