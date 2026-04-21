# core/chat/urls.py

from django.urls import path
from core.chat.views import (
    ChatRoomListView,
    ChatCreateRoomView,
    ChatMessageListView,
    ChatSendMessageView,
    ChatMarkReadView,
)

urlpatterns = [
    path("rooms/", ChatRoomListView.as_view()),
    path("rooms/create/", ChatCreateRoomView.as_view()),
    path("rooms/<int:room_id>/messages/", ChatMessageListView.as_view()),
    path("rooms/<int:room_id>/send/", ChatSendMessageView.as_view()),
    path("rooms/<int:room_id>/read/", ChatMarkReadView.as_view()),
]