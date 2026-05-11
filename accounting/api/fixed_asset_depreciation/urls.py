# accounting/api/fixed_asset_depreciation/urls.py

from django.urls import path

from .views import (
    FixedAssetBulkDepreciationAPIView,
    FixedAssetDepreciationListAPIView,
)

urlpatterns = [
    path("", FixedAssetDepreciationListAPIView.as_view()),
    path("run/", FixedAssetBulkDepreciationAPIView.as_view()),
]
