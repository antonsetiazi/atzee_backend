# accounting/api/taxes/urls.py

from django.urls import path

from .views import (
    TaxListAPIView,
    TaxCreateAPIView,
)

urlpatterns = [

    path(
        "",
        TaxListAPIView.as_view()
    ),

    path(
        "create/",
        TaxCreateAPIView.as_view()
    ),

]