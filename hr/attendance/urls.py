from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hr.attendance.views import AttendanceViewSet


router = DefaultRouter()
router.register(r"attendance", AttendanceViewSet, basename="attendance")

urlpatterns = [
    path("", include(router.urls)),
]


"""
| Method | Endpoint            | Fungsi            |
| ------ | ------------------- | ----------------- |
| GET    | `/attendance/`      | List attendance   |
| POST   | `/attendance/`      | Create attendance |
| GET    | `/attendance/{id}/` | Detail attendance |
| PUT    | `/attendance/{id}/` | Update            |
| PATCH  | `/attendance/{id}/` | Partial update    |
| DELETE | `/attendance/{id}/` | Soft delete       |
"""