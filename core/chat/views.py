# core/chat/views.py

from django.db.models import Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from core.chat.models import (
    ChatRoom,
    ChatParticipant,
    ChatMessage,
)
from core.chat.serializers import (
    ChatRoomSerializer,
    ChatMessageSerializer,
)
from core.chat.services import ChatService
from core.tenants.services import TenantService
from core.chat.services import generate_room_key


# ======================================================
# CREATE ROOM
# ======================================================
class ChatCreateRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tenant = TenantService.get_current_tenant(request)

        my_id = str(request.user.id)
        target_user_id = str(request.data.get("targetUserId"))

        context_type = request.data.get("context_type")
        context_id = request.data.get("context_id")

        # 🔥 1. buat room key deterministic
        room_key = generate_room_key(
            my_id,
            target_user_id,
            context_type,
            context_id,
        )

        # 🔥 2. cari room berdasarkan key
        found_room = ChatRoom.objects.filter(
            tenant=tenant,
            room_key=room_key,
            is_deleted=False,
        ).first()

        # 🔥 3. kalau sudah ada → return
        if found_room:
            return Response(ChatRoomSerializer(found_room).data)

        # 🔥 4. create baru
        room = ChatRoom.objects.create(
            tenant=tenant,
            type="direct",
            context_type=context_type,
            context_id=context_id,
            room_key=room_key,   # 🔥 PENTING
            created_by=request.user,
        )

        ChatParticipant.objects.create(
            room=room,
            user=request.user,
            role="user",
        )

        ChatParticipant.objects.create(
            room=room,
            user_id=target_user_id,
            role="partner",
        )

        room.refresh_from_db()

        return Response(ChatRoomSerializer(room).data)


# ======================================================
# ROOM LIST
# ======================================================
class ChatRoomListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        rooms = (
            ChatRoom.objects.filter(
                tenant=tenant,
                participants__user=request.user,
                is_deleted=False,
            )
            .prefetch_related("participants__user")
            .distinct()
        )

        data = ChatRoomSerializer(
            rooms,
            many=True,
        ).data

        return Response(data)


# ======================================================
# MESSAGE LIST
# ======================================================
class ChatMessageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, room_id):
        is_member = ChatParticipant.objects.filter(
            room_id=room_id,
            user=request.user,
        ).exists()

        if not is_member:
            return Response(
                {"detail": "Forbidden"},
                status=403,
            )

        messages = ChatMessage.objects.filter(
            room_id=room_id,
            is_deleted=False,
        ).select_related("sender")

        return Response(
            ChatMessageSerializer(
                messages,
                many=True,
            ).data
        )


# ======================================================
# SEND
# ======================================================
class ChatSendMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, room_id):
        content = request.data.get("content", "").strip()

        if not content:
            return Response(
                {"detail": "content required"},
                status=400,
            )

        is_member = ChatParticipant.objects.filter(
            room_id=room_id,
            user=request.user,
        ).exists()

        if not is_member:
            return Response(
                {"detail": "Forbidden"},
                status=403,
            )

        msg = ChatService.send_message(
            room_id=room_id,
            sender=request.user,
            content=content,
        )

        return Response(
            ChatMessageSerializer(msg).data
        )


# ======================================================
# READ
# ======================================================
class ChatMarkReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, room_id):
        ChatService.mark_room_read(
            room_id=room_id,
            user=request.user,
        )

        return Response({"success": True})