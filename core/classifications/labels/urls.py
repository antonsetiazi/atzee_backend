# core/classifications/labels/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.classifications.labels.views import LabelViewSet

router = DefaultRouter()
router.register("labels", LabelViewSet, basename="label")

urlpatterns = [
    path("", include(router.urls)),
]
