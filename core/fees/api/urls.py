# core/fees/api/urls.py

from rest_framework.routers import DefaultRouter
from .views import FeeConfigViewSet

router = DefaultRouter()
router.register(r"fees", FeeConfigViewSet)

urlpatterns = router.urls