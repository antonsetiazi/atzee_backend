# core/activity/api/urls.py

from rest_framework.routers import DefaultRouter

from core.activity.api.views import ActivityViewSet

router = DefaultRouter()

router.register(r"", ActivityViewSet, basename="activity")

urlpatterns = router.urls
