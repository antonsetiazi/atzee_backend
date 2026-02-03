# accounting/chart_of_accounts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounting.chart_of_accounts.views import ChartOfAccountViewSet


router = DefaultRouter()
router.register(r"chart-of-accounts", ChartOfAccountViewSet, basename="chart-of-account")

urlpatterns = [
    path("", include(router.urls)),
]
