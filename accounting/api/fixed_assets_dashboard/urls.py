from django.urls import path

from .views import (
    AssetCategorySummaryAPIView,
    FixedAssetDashboardSummaryAPIView,
    MonthlyDepreciationSummaryAPIView,
)

urlpatterns = [
    path("summary/", FixedAssetDashboardSummaryAPIView.as_view()),
    path("category-summary/", AssetCategorySummaryAPIView.as_view()),
    path("monthly-depreciation/", MonthlyDepreciationSummaryAPIView.as_view()),
]
