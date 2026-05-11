# accounting/api/asset_categories/urls.py

from django.urls import path

from .views import (
    AssetCategoryCreateAPIView,
    AssetCategoryDetailAPIView,
    AssetCategoryListAPIView,
)

urlpatterns = [
    path("", AssetCategoryListAPIView.as_view()),
    path("create/", AssetCategoryCreateAPIView.as_view()),
    path("<uuid:category_id>/", AssetCategoryDetailAPIView.as_view()),
]
