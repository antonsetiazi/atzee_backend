from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounting.ledger.views import LedgerEntryViewSet


router = DefaultRouter()
router.register(
    r"ledger",
    LedgerEntryViewSet,
    basename="ledger"
)

urlpatterns = [
    path("", include(router.urls)),
]
