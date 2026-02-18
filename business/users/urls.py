# business/users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.users.views import BusinessUserViewSet

router = DefaultRouter()
router.register(r"users", BusinessUserViewSet, basename="business-user")

urlpatterns = [
    path("", include(router.urls)),
]
