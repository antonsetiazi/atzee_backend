# accounting/api/journals/urls.py

from django.urls import path

from .views import (
    JournalCreateAPIView,
    JournalListAPIView,
    JournalDetailAPIView,
)

urlpatterns = [
    path("create/", JournalCreateAPIView.as_view()),

    path("", JournalListAPIView.as_view()),

    path(
        "<uuid:journal_id>/",
        JournalDetailAPIView.as_view()
    ),
]