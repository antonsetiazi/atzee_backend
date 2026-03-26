# business/products/serializers.py

from rest_framework import serializers
from business.products.models import Product, PartnerOffering

# ==============================
# 🔥 BASE VALIDATION
# ==============================
VALID_PRODUCT_TYPES = {
    Product.TYPE_GOOD,
    Product.TYPE_SERVICE,
}

def normalize_str(value):
    if value is None:
        return None
    value = value.strip()
    return value or None

# ==============================
# 🔥 CREATE
# ==============================
class ProductCreateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(max_length=255)
    product_type = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    extensions = serializers.JSONField(required=False)

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Name is required.")
        return value

    def validate_product_type(self, value):
        value = normalize_str(value)

        if value and value not in VALID_PRODUCT_TYPES:
            raise serializers.ValidationError("Invalid product type.")

        return value

    def validate_code(self, value):
        return normalize_str(value)

    def validate_description(self, value):
        return normalize_str(value)
    

# ==============================
# 🔥 UPDATE
# ==============================
class ProductUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(required=False, allow_blank=True)
    product_type = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    extensions = serializers.JSONField(required=False)

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_product_type(self, value):
        value = normalize_str(value)

        if value and value not in VALID_PRODUCT_TYPES:
            raise serializers.ValidationError("Invalid product type.")

        return value

    def validate_code(self, value):
        return normalize_str(value)

    def validate_description(self, value):
        return normalize_str(value)
    

# ==============================
# 🔥 DETAIL
# ==============================
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "code",
            "name",
            "product_type",
            "description",
            "is_active",
            "extensions",
            "created_at",
            "updated_at",
        ]


# ==============================
# 🔥 LIST
# ==============================
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "code",
            "name",
            "product_type",
            "is_active",
        ]


# ==============================
# 🔥 OFFERING CARD (SERVICE UI)
# ==============================
class PartnerOfferingCardSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    description = serializers.CharField(source="product.description")

    class Meta:
        model = PartnerOffering
        fields = [
            "id",  # offering_id
            "product_name",
            "description",
            "price",
            "duration_minutes",
        ]