# core/chat/services.py

from django.db import transaction
from django.db.models import Count, F, Q
from django.utils import timezone

from core.chat.models import (
    ChatRoom,
    ChatParticipant,
    ChatMessage,
    ChatMessageRead,
)
from core.tenants.services import TenantService
from core.users.models import User


def generate_room_key(user1, user2, context_type, context_id):
    users = sorted([str(user1), str(user2)])
    return f"{context_type}:{context_id}:{users[0]}:{users[1]}"


class ChatService:
    """
    Centralized business logic for chat.
    """

    # ======================================================
    # ROOM
    # ======================================================
    @classmethod
    @transaction.atomic
    def get_or_create_direct_room(
        cls,
        *,
        request,
        target_user_id,
        context_type=None,
        context_id=None,
    ):
        user = request.user
        tenant = TenantService.get_current_tenant(request)

        # cari room direct existing yg berisi tepat 2 participant
        qs = (
            ChatRoom.objects.filter(
                tenant=tenant,
                type="direct",
                is_deleted=False,
                participants__user=user,
            )
            .filter(participants__user_id=target_user_id)
            .annotate(total_participants=Count("participants"))
            .filter(total_participants=2)
            .distinct()
        )

        if context_type and context_id:
            qs = qs.filter(
                context_type=context_type,
                context_id=str(context_id),
            )
        else:
            qs = qs.filter(
                Q(context_type__isnull=True) | Q(context_type=""),
                Q(context_id__isnull=True) | Q(context_id=""),
            )

        room = qs.first()
        if room:
            return room

        room = ChatRoom.objects.create(
            tenant=tenant,
            type="direct",
            context_type=context_type,
            context_id=context_id,
            created_by=user,
            last_timestamp=timezone.now(),
        )

        ChatParticipant.objects.create(
            room=room,
            user=user,
            role="user",
        )

        target_user = User.objects.get(pk=target_user_id)

        ChatParticipant.objects.create(
            room=room,
            user=target_user,
            role="partner",
        )

        return room

    # ======================================================
    # SEND MESSAGE
    # ======================================================
    @classmethod
    @transaction.atomic
    def send_message(
        cls,
        *,
        room_id,
        sender,
        content,
        msg_type="text",
    ):
        room = ChatRoom.objects.get(
            pk=room_id,
            is_deleted=False,
        )

        msg = ChatMessage.objects.create(
            room=room,
            sender=sender,
            type=msg_type,
            content=content,
            status="sent",
        )

        room.last_message = content
        room.last_message_type = msg_type
        room.last_sender = sender
        room.last_timestamp = msg.created_at
        room.message_count = F("message_count") + 1
        room.save(
            update_fields=[
                "last_message",
                "last_message_type",
                "last_sender",
                "last_timestamp",
                "message_count",
            ]
        )

        ChatParticipant.objects.filter(
            room=room
        ).exclude(
            user=sender
        ).update(
            unread_count=F("unread_count") + 1
        )

        room.refresh_from_db()

        return msg

    # ======================================================
    # MARK READ
    # ======================================================
    @classmethod
    @transaction.atomic
    def mark_room_read(
        cls,
        *,
        room_id,
        user,
    ):
        ChatParticipant.objects.filter(
            room_id=room_id,
            user=user,
        ).update(
            unread_count=0,
            last_seen_at=timezone.now(),
        )

        unread_messages = ChatMessage.objects.filter(
            room_id=room_id,
            is_deleted=False,
        ).exclude(sender=user)

        unread_messages.update(status="read")

        for msg in unread_messages:
            ChatMessageRead.objects.get_or_create(
                message=msg,
                user=user,
            )