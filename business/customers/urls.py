# business/customers/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.customers.views import CustomerViewSet


router = DefaultRouter()
router.register(r"customers", CustomerViewSet, basename="customer")

urlpatterns = [
    path("", include(router.urls)),
]


"""
| Method | Endpoint           | Fungsi          |
| ------ | ------------------ | --------------- |
| GET    | `/customers/`      | List customer   |
| POST   | `/customers/`      | Create customer |
| GET    | `/customers/{id}/` | Detail customer |
| PUT    | `/customers/{id}/` | Update          |
| PATCH  | `/customers/{id}/` | Partial update  |
| DELETE | `/customers/{id}/` | Soft delete     |
"""