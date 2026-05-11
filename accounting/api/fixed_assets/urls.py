# accounting/api/fixed_assets/urls.py

from django.urls import path

from .views import (
    FixedAssetActivateAPIView,
    FixedAssetCreateAPIView,
    FixedAssetDepreciateAPIView,
    FixedAssetDetailAPIView,
    FixedAssetListAPIView,
)

urlpatterns = [
    path("", FixedAssetListAPIView.as_view()),
    path("create/", FixedAssetCreateAPIView.as_view()),
    path("<uuid:asset_id>/", FixedAssetDetailAPIView.as_view()),
    path("<uuid:asset_id>/activate/", FixedAssetActivateAPIView.as_view()),
    path("<uuid:asset_id>/depreciate/", FixedAssetDepreciateAPIView.as_view()),
]
