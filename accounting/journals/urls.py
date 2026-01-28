from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounting.journals.views import JournalViewSet


router = DefaultRouter()
router.register(r"journals", JournalViewSet, basename="journal")

urlpatterns = [
    path("", include(router.urls)),
]


"""
| Method | Endpoint                   | Fungsi          |
| ------ | -------------------------- | --------------- |
| GET    | `/journals/`               | List journals   |
| GET    | `/journals/{id}/`          | Detail journal  |
| POST   | `/journals/{id}/reverse/`  | Reverse journal |
"""