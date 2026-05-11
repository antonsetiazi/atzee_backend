# accounting/api/payables_dashboard/urls.py

from django.urls import path

from .views import PayablesDashboardAPIView

urlpatterns = [
    path("", PayablesDashboardAPIView.as_view()),
]
