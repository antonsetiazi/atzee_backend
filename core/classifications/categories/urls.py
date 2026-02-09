# core/classifications/categories/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.classifications.categories.views import CategoryViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
