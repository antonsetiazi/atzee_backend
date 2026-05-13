# core/activity/api/serializers.py

from rest_framework import serializers

from core.activity.models import (
    Activity,
    ActivityAttachment,
    ActivityComment,
    ActivityReaction,
)


class ActivityAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityAttachment

        fields = [
            "id",
            "file",
            "file_name",
            "file_size",
            "mime_type",
            "created_at",
        ]


class ActivityCommentSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model = ActivityComment

        fields = [
            "id",
            "content",
            "is_internal",
            "created_by",
            "created_by_name",
            "created_at",
        ]

    def get_created_by_name(self, obj):
        if not obj.created_by:
            return None

        return getattr(obj.created_by, "full_name", obj.created_by.username)


class ActivityReactionSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = ActivityReaction

        fields = [
            "id",
            "reaction",
            "user",
            "user_name",
            "created_at",
        ]

    def get_user_name(self, obj):
        if not obj.user:
            return None

        return getattr(obj.user, "full_name", obj.user.username)


class ActivitySerializer(serializers.ModelSerializer):
    """
    Universal activity timeline serializer.
    """

    created_by_name = serializers.SerializerMethodField()
    actor_name = serializers.SerializerMethodField()

    attachments = ActivityAttachmentSerializer(many=True, read_only=True)

    comments = ActivityCommentSerializer(many=True, read_only=True)

    reactions = ActivityReactionSerializer(many=True, read_only=True)

    class Meta:
        model = Activity

        fields = [
            "id",
            # =================================================
            # TARGET
            # =================================================
            "target_type",
            "target_id",
            # =================================================
            # EVENT
            # =================================================
            "event",
            "title",
            "description",
            "metadata",
            # =================================================
            # CLASSIFICATION
            # =================================================
            "visibility",
            "severity",
            "source",
            # =================================================
            # FLAGS
            # =================================================
            "is_pinned",
            "is_immutable",
            # =================================================
            # ACTORS
            # =================================================
            "created_by",
            "created_by_name",
            "actor",
            "actor_name",
            # =================================================
            # RELATIONS
            # =================================================
            "attachments",
            "comments",
            "reactions",
            # =================================================
            # TIMESTAMPS
            # =================================================
            "created_at",
            "updated_at",
        ]

    def get_created_by_name(self, obj):
        if not obj.created_by:
            return None

        return getattr(obj.created_by, "full_name", obj.created_by.username)

    def get_actor_name(self, obj):
        if not obj.actor:
            return None

        return getattr(obj.actor, "full_name", obj.actor.username)
