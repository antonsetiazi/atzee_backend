# accounting/api/receivables_dashboard/urls.py

from django.urls import path

from .views import (
    ReceivableDashboardAPIView,
)

urlpatterns = [
    path("", ReceivableDashboardAPIView.as_view()),
]
