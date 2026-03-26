# discovery/serializers/product_listing_serializer.py

from rest_framework import serializers
from business.products.models import PartnerOffering


class ProductListingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name")
    image = serializers.SerializerMethodField()

    class Meta:
        model = PartnerOffering
        fields = [
            "id",
            "name",
            "price",
            "image",
        ]

    def get_image(self, obj):
        return obj.product.extensions.get(
            "image",
            "https://placehold.co/600x400"
        )