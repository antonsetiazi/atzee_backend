# core/widgets/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.widgets.views import WidgetViewSet

router = DefaultRouter()
router.register(r"widgets", WidgetViewSet, basename="widget")

urlpatterns = [
    path("", include(router.urls)),
]
