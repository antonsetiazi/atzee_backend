from rest_framework import serializers
from business.products.models import Product, PartnerProduct


class ProductCreateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(max_length=255)
    product_type = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)  
    extensions = serializers.JSONField(required=False) 
    

class ProductUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(max_length=255)
    product_type = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    extensions = serializers.JSONField(required=False) 
    

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


class PartnerServiceCardSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    description = serializers.CharField(source="product.description")

    class Meta:
        model = PartnerProduct
        fields = [
            "id",                # 🔥 partner_product_id
            "product_name",
            "description",
            "price",
            "duration_minutes",
        ]