# core/schedule/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.schedule.events.views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]
