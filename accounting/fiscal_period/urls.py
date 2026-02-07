# accounting/fiscal_period/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounting.fiscal_period.views import FiscalPeriodViewSet

router = DefaultRouter()
router.register(r"fiscal-periods", FiscalPeriodViewSet, basename="fiscal-period")

urlpatterns = [
    path("", include(router.urls)),
]


# | Method | URL                                          | Deskripsi                               |
# | ------ | -------------------------------------------- | --------------------------------------- |
# | GET    | `/api/accounting/fiscal-periods/`            | List fiscal periods                     |
# | GET    | `/api/accounting/fiscal-periods/<id>/`       | Detail period                           |
# | POST   | `/api/accounting/fiscal-periods/`            | Create new period                       |
# | PATCH  | `/api/accounting/fiscal-periods/<id>/`       | Update period (hanya sebelum closed)    |
# | POST   | `/api/accounting/fiscal-periods/<id>/close/` | Close period & generate closing journal |
