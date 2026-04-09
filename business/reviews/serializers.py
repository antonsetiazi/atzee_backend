# business/reviews/serializers.py

from rest_framework import serializers
from .models import Review


class CreateReviewSerializer(serializers.Serializer):
    booking_id = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField(required=False, allow_blank=True)


class ReviewOutputSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.full_name")

    class Meta:
        model = Review
        fields = [
            "id",
            "booking_id",
            "rating",
            "comment",
            "created_at",
            "user_name",
        ]