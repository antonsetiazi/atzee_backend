# business/products/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.products.views import ProductViewSet


router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]


"""
| Method | Endpoint           | Fungsi          |
| ------ | ------------------ | --------------- |
| GET    | `/products/`      | List product   |
| POST   | `/products/`      | Create product |
| GET    | `/products/{id}/` | Detail product |
| PUT    | `/products/{id}/` | Update          |
| PATCH  | `/products/{id}/` | Partial update  |
| DELETE | `/products/{id}/` | Soft delete     |
"""