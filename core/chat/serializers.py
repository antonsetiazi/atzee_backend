# core/chat/serializers.py

from rest_framework import serializers
from core.chat.models import (
    ChatRoom,
    ChatParticipant,
    ChatMessage,
)


# ==========================================
# PARTICIPANT
# ==========================================
class ChatParticipantSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="user.id")
    name = serializers.CharField(source="user.full_name")

    class Meta:
        model = ChatParticipant
        fields = [
            "id",
            "name",
            "role",
            "unread_count",
        ]


# ==========================================
# ROOM LIST
# ==========================================
class ChatRoomSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()
    participants_detail = ChatParticipantSerializer(
        many=True,
        source="participants"
    )

    class Meta:
        model = ChatRoom
        fields = [
            "id",
            "type",
            "status",
            "title",

            "context_type",
            "context_id",

            "last_message",
            "last_timestamp",

            "participants",
            "participants_detail",
        ]

    def get_participants(self, obj):
        return [
            str(x.user_id)
            for x in obj.participants.all()
        ]


# ==========================================
# MESSAGE
# ==========================================
class ChatMessageSerializer(serializers.ModelSerializer):
    room_id = serializers.CharField(source="room.id")
    sender_id = serializers.SerializerMethodField()

    class Meta:
        model = ChatMessage
        fields = [
            "id",
            "room_id",
            "sender_id",
            "type",
            "content",
            "status",
            "created_at",
        ]

    def get_sender_id(self, obj):
        if obj.sender:
            return str(obj.sender.id)
        return "system"