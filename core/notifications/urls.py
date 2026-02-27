# core/notifications/urls.py

from django.urls import path
from core.notifications.views import (
    NotificationListView,
    NotificationMarkReadView,
    NotificationUnreadCountView,
    NotificationMarkAllReadView,
)

urlpatterns = [
    path("", NotificationListView.as_view()),
    path("unread-count/", NotificationUnreadCountView.as_view()),
    path("<int:pk>/read/", NotificationMarkReadView.as_view()),
    path("mark-all-read/", NotificationMarkAllReadView.as_view()),
]
