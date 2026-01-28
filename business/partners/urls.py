from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.partners.views import PartnerViewSet


router = DefaultRouter()
router.register(r"partners", PartnerViewSet, basename="partner")

urlpatterns = [
    path("", include(router.urls)),
]


"""
| Method | Endpoint          | Fungsi         |
| ------ | ----------------- | -------------- |
| GET    | `/partners/`      | List partner   |
| POST   | `/partners/`      | Create partner |
| GET    | `/partners/{id}/` | Detail partner |
| PUT    | `/partners/{id}/` | Update         |
| PATCH  | `/partners/{id}/` | Partial update |
| DELETE | `/partners/{id}/` | Soft delete    |
"""