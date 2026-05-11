# accounting/api/asset_disposals/urls.py

from django.urls import path

from .views import (
    AssetDisposalCreateAPIView,
    AssetDisposalDetailAPIView,
    AssetDisposalListAPIView,
)

urlpatterns = [
    path("", AssetDisposalListAPIView.as_view()),
    path("create/", AssetDisposalCreateAPIView.as_view()),
    path("<uuid:disposal_id>/", AssetDisposalDetailAPIView.as_view()),
]
