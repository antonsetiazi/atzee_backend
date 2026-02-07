# business/documents/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.documents.views import (
    DocumentViewSet,
    DocumentTypeViewSet
)


router = DefaultRouter()
router.register(r"documents", DocumentViewSet, basename="document")
router.register(r"document-types", DocumentTypeViewSet, basename="document-type")

urlpatterns = [
    path("", include(router.urls)),
    path("documents/<int:pk>/issue/", DocumentViewSet.as_view({"post": "issue"}), name="document-issue"),
    path("documents/<int:pk>/void/", DocumentViewSet.as_view({"post": "void"}), name="document-void"),
]


"""
| Method | Endpoint                         | Fungsi              |
|------- |----------------------------------|---------------------|
| GET    | /documents/                      | List documents      |
| POST   | /documents/                      | Create (draft)      |
| GET    | /documents/{id}/                 | Detail              |
| POST   | /documents/{id}/issue/           | Issue document      |
| POST   | /documents/{id}/void/            | Void document       |
| GET    | /document-types/                 | List document types |

"""