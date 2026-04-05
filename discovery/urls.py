# discovery/urls.py

from django.urls import path
from discovery.views import (
    ProductListingView,
    ServiceListingView,
    ServiceDetailView,
    CategoryListView,
)

urlpatterns = [
    path("listings/products/", ProductListingView.as_view()),
    path("listings/services/", ServiceListingView.as_view()),
    path("services/<int:partner_id>/", ServiceDetailView.as_view()),
    path("categories/", CategoryListView.as_view()),
]