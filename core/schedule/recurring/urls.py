# core/schedule/recurring/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.schedule.recurring.views import RecurringRuleViewSet

router = DefaultRouter()
router.register(r'recurring-rules', RecurringRuleViewSet, basename='recurring-rule')

urlpatterns = [
    path('', include(router.urls)),
]
