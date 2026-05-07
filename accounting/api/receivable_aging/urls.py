# accounting/api/receivable_aging/urls.py

from django.urls import path

from .views import (
    ReceivableAgingAPIView
)

urlpatterns = [

    path(
        "",
        ReceivableAgingAPIView.as_view()
    ),

]