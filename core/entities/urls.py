# core/entities/urls.py

from django.urls import path
from .views import EntityQueryView

urlpatterns = [
    path("<str:entity_key>/query/", EntityQueryView.as_view()),
]
