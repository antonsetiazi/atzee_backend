# core/chat/models.py

from django.db import models
from django.db.models import Q

from core.users.models import User
from core.tenants.models import Tenant


# ==========================================================
# CHAT ROOM
# ==========================================================
class ChatRoom(models.Model):
    """
    Master room percakapan.

    direct         = percakapan biasa user ↔ partner
    transactional  = chat yang terkait booking/order/payment
    support        = admin/customer support
    group          = future ready
    """

    ROOM_TYPES = (
        ("direct", "direct"),
        ("transactional", "transactional"),
        ("support", "support"),
        ("group", "group"),
    )

    STATUS_CHOICES = (
        ("active", "active"),
        ("archived", "archived"),
        ("closed", "closed"),
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="chat_rooms",
        null=True,
        blank=True,
    )

    type = models.CharField(
        max_length=30,
        choices=ROOM_TYPES,
        default="direct",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
    )

    # contoh:
    # booking / order / payment / service
    context_type = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    # id object terkait
    context_id = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    room_key = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )

    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="optional title for support/group room",
    )

    # cache preview frontend
    last_message = models.TextField(
        null=True,
        blank=True,
    )

    last_message_type = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    last_sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="chat_rooms_last_sender",
    )

    last_timestamp = models.DateTimeField(
        null=True,
        blank=True,
    )

    message_count = models.PositiveIntegerField(default=0)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_chat_rooms",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "core_chat_rooms"
        ordering = ["-last_timestamp", "-created_at"]
        indexes = [
            models.Index(fields=["tenant"]),
            models.Index(fields=["type"]),
            models.Index(fields=["status"]),
            models.Index(fields=["context_type", "context_id"]),
            models.Index(fields=["last_timestamp"]),
            models.Index(fields=["is_deleted"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["room_key"],
                name="unique_chat_room_key"
            )
        ]
        

    def __str__(self):
        return f"Room #{self.id} ({self.type})"


# ==========================================================
# CHAT PARTICIPANT
# ==========================================================
class ChatParticipant(models.Model):
    """
    User yang join ke room.
    unread_count disimpan per user supaya cepat di frontend.
    """

    ROLE_CHOICES = (
        ("user", "user"),
        ("partner", "partner"),
        ("admin", "admin"),
        ("staff", "staff"),
    )

    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name="participants",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="chat_participations",
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="user",
    )

    unread_count = models.PositiveIntegerField(default=0)

    is_muted = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    joined_at = models.DateTimeField(auto_now_add=True)
    last_seen_at = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_chat_participants"
        unique_together = ("room", "user")
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["room"]),
            models.Index(fields=["user", "is_archived"]),
            models.Index(fields=["user", "unread_count"]),
        ]

    def __str__(self):
        return f"{self.user_id} in Room {self.room_id}"


# ==========================================================
# CHAT MESSAGE
# ==========================================================
class ChatMessage(models.Model):
    """
    Pesan chat.
    """

    MESSAGE_TYPES = (
        ("text", "text"),
        ("image", "image"),
        ("file", "file"),
        ("audio", "audio"),
        ("video", "video"),
        ("system", "system"),
    )

    STATUS_CHOICES = (
        ("sent", "sent"),
        ("delivered", "delivered"),
        ("read", "read"),
    )

    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name="messages",
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sent_chat_messages",
    )

    type = models.CharField(
        max_length=20,
        choices=MESSAGE_TYPES,
        default="text",
    )

    content = models.TextField(
        blank=True,
        default="",
    )

    # untuk file/image/audio/video
    file = models.FileField(
        upload_to="chat/",
        null=True,
        blank=True,
    )

    file_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    file_size = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    mime_type = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="sent",
    )

    # reply message
    reply_to = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="replies",
    )

    # extra payload fleksibel
    payload = models.JSONField(
        null=True,
        blank=True,
        help_text="future metadata",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "core_chat_messages"
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["room"]),
            models.Index(fields=["sender"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["room", "created_at"]),
            models.Index(fields=["status"]),
            models.Index(fields=["is_deleted"]),
        ]

    def __str__(self):
        return f"Msg #{self.id} Room {self.room_id}"


# ==========================================================
# MESSAGE READ LOG (optional production level)
# ==========================================================
class ChatMessageRead(models.Model):
    """
    Untuk read receipt akurat multi-user.
    Bisa dipakai untuk double tick biru.
    """

    message = models.ForeignKey(
        ChatMessage,
        on_delete=models.CASCADE,
        related_name="read_logs",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="chat_read_logs",
    )

    read_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "core_chat_message_reads"
        unique_together = ("message", "user")
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["message"]),
        ]

    def __str__(self):
        return f"Read msg {self.message_id} by {self.user_id}"


# ==========================================================
# PRESENCE
# ==========================================================
class ChatPresence(models.Model):
    """
    Online status realtime fallback database.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="chat_presence",
    )

    is_online = models.BooleanField(default=False)
    last_seen_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "core_chat_presence"

    def __str__(self):
        return f"{self.user_id} online={self.is_online}"