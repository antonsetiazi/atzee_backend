# core/lookups/urls.py

from django.urls import path
from .views import LookupView

urlpatterns = [
    path("<str:key>/", LookupView.as_view()),
]
