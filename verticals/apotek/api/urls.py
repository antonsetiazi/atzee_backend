# verticals/apotek/api/urls.py

from django.urls import path
from .customer_profile import ApotekCustomerProfileAPI

urlpatterns = [
    path(
        "customers/<int:customer_id>/apotek-profile/",
        ApotekCustomerProfileAPI.as_view(),
        name="apotek-customer-profile",
    ),
]
