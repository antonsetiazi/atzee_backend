# discovery/serializers/service_detail_serializer.py

from rest_framework import serializers


class ServiceDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="partner.id")
    name = serializers.CharField(source="partner.name")

    rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    
    resource_id = serializers.SerializerMethodField()

    avatar_url = serializers.SerializerMethodField()
    offerings = serializers.SerializerMethodField()

    specialization = serializers.SerializerMethodField()
    experience_years = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    working_hours = serializers.SerializerMethodField()
    
    
    def get_resource_id(self, obj):
        profile = obj.get("service_profile")
        return str(profile.id) if profile else None
    
    def get_avatar_url(self, obj):
        request = self.context.get("request")
        images = obj.get("images")

        if not images or not images.exists():
            return "https://placehold.co/600x400"

        file_obj = images.first()

        if request:
            return request.build_absolute_uri(
                f"/api/files/{file_obj.id}/download/"
            )

        return f"/api/files/{file_obj.id}/download/"

    def get_offerings(self, obj):
        offerings = obj.get("offerings")

        return [
            {
                "product_id": o.product.id,
                "product_name": o.product.name,
                "price": int(o.price),
                "duration_minutes": o.duration_minutes,
            }
            for o in offerings
        ]
    
    def get_specialization(self, obj):
        profile = obj.get("service_profile")
        return profile.specialization if profile else None

    def get_experience_years(self, obj):
        profile = obj.get("service_profile")
        return profile.experience_years if profile else 0

    def get_bio(self, obj):
        profile = obj.get("service_profile")
        return profile.bio if profile else None

    def get_working_hours(self, obj):
        profile = obj.get("service_profile")

        if profile and profile.working_hours:
            return profile.working_hours

        return {
            "start": 8,
            "end": 18
        }
    
    def get_rating(self, obj):
        partner = obj.get("partner")
        if not partner:
            return 0

        return float(partner.rating_avg or 0)


    def get_rating_count(self, obj):
        partner = obj.get("partner")
        if not partner:
            return 0

        return partner.rating_count or 0