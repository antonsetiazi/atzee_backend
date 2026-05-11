# accounting/api/accounts/urls.py

from django.urls import path

from .views import (
    AccountListAPIView,
)

urlpatterns = [
    path("", AccountListAPIView.as_view()),
]
