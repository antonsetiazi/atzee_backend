# core/entities/urls.py

from django.urls import path
from .views import EntityQueryView

urlpatterns = [
    path("<str:domain>/<str:entity>/query/", EntityQueryView.as_view(), name="entity-query"),
]
