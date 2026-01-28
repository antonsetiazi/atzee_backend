from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hr.employees.views import EmployeeViewSet


router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("", include(router.urls)),
]


"""
| Method | Endpoint           | Fungsi          |
| ------ | ------------------ | --------------- |
| GET    | `/employees/`      | List employee   |
| POST   | `/employees/`      | Create employee |
| GET    | `/employees/{id}/` | Detail employee |
| PUT    | `/employees/{id}/` | Update          |
| PATCH  | `/employees/{id}/` | Partial update  |
| DELETE | `/employees/{id}/` | Soft delete     |
"""