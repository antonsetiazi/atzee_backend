from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.transactions.views import TransactionViewSet


router = DefaultRouter()
router.register(r"transactions", TransactionViewSet, basename="transaction")

urlpatterns = [
    path("", include(router.urls)),
]


"""
| Method | Endpoint                       | Fungsi              |
| ------ | ------------------------------ | ------------------- |
| GET    | `/transactions/`               | List                |
| POST   | `/transactions/`               | Create              |
| GET    | `/transactions/{id}/`          | Detail              |

| POST   | `/transactions/{id}/add-item/` | add line item       |
| POST   | `/transactions/{id}/confirm/`  | confirm transaction |
| POST   | `/transactions/{id}/cancel/`   | cancel transaction  |
"""