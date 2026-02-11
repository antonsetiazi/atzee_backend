# core/classifications/attributes/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.classifications.attributes.views import (
    AttributeViewSet,
    AttributeOptionViewSet,
)

router = DefaultRouter()
router.register("attributes", AttributeViewSet, basename="attribute")

attribute_option_list = AttributeOptionViewSet.as_view({
    "get": "list",
    "post": "create",
})

attribute_option_detail = AttributeOptionViewSet.as_view({
    "get": "retrieve",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("", include(router.urls)),
    # ✅ LIST + CREATE
    path(
        "attributes/<int:attribute_id>/options/",
        attribute_option_list,
        name="attribute-option-list",
    ),

    # ✅ UPDATE + DELETE
    path(
        "attributes/<int:attribute_id>/options/<int:pk>/",
        attribute_option_detail,
        name="attribute-option-detail",
    ),
]
