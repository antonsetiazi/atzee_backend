# discovery/serializers/service_listing_serializer.py

from rest_framework import serializers
from core.files import selectors


class ServiceListingSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="partner_id")
    name = serializers.CharField(source="partner__name")
    image = serializers.SerializerMethodField()
    starting_price = serializers.IntegerField()
    service_count = serializers.IntegerField()
    priceLabel = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    

    def get_image(self, obj):
        request = self.context.get("request")
        tenant = self.context.get("tenant")

        files_qs = selectors.get_files_by_relation(
            tenant=tenant,
            related_entity="partner_image",
            related_id=str(obj["partner_id"]),
        ).order_by("created_at")

        if not files_qs.exists():
            return "https://placehold.co/600x400"

        file_obj = files_qs.first()

        if request:
            return request.build_absolute_uri(
                f"/api/files/{file_obj.id}/download/"
            )

        return f"/api/files/{file_obj.id}/download/"


    def get_starting_price(self, obj):
        return int(obj["starting_price"])

    def get_priceLabel(self, obj):
        return f"Mulai dari Rp {int(obj['starting_price']):,}"
    
    def get_city(self, obj):
        name = obj.get("partner__city__name")

        if not name:
            return "Lokasi belum diatur"

        # 🔥 normalize nama kota Indonesia
        replacements = [
            "Kota Administrasi ",
            "Kabupaten ",
            "Kota ",
        ]

        for r in replacements:
            if name.startswith(r):
                return name.replace(r, "", 1)

        return name