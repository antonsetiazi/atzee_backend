# core/entities/urls.py

from django.urls import path
from .views import EntityQueryView, EntityExecuteView

urlpatterns = [
    path("<str:domain>/<str:entity>/query/", EntityQueryView.as_view(), name="entity-query"),
    path("<str:domain>/<str:entity>/execute/", EntityExecuteView.as_view(), name="entity-execute"),
]
