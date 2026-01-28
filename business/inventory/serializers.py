from decimal import Decimal

from rest_framework import serializers

from business.inventory import services, selectors
from business.inventory.models import Warehouse, StockItem, StockMovement
from business.products.models import Product


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            "id",
            "name",
            "code",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields


class WarehouseCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(default=True)


class StockItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product.id")
    product_name = serializers.CharField(source="product.name")

    class Meta:
        model = StockItem
        fields = [
            "id",
            "product_id",
            "product_name",
            "quantity",
        ]
        read_only_fields = fields


class StockMovementBaseSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    warehouse_id = serializers.IntegerField()
    quantity = serializers.DecimalField(max_digits=15, decimal_places=3)
    note = serializers.CharField(required=False, allow_blank=True)


class StockInSerializer(StockMovementBaseSerializer):
    def save(self, **kwargs):
        request = self.context["request"]
        tenant = request.tenant
        user = request.user

        product = Product.objects.get(id=self.validated_data["product_id"])
        warehouse = Warehouse.objects.get(id=self.validated_data["warehouse_id"])

        return services.stock_in(
            tenant=tenant,
            user=user,
            product=product,
            warehouse=warehouse,
            quantity=self.validated_data["quantity"],
            note=self.validated_data.get("note", ""),
        )
    

class StockOutSerializer(StockMovementBaseSerializer):
    def save(self, **kwargs):
        request = self.context["request"]
        tenant = request.tenant
        user = request.user

        product = Product.objects.get(id=self.validated_data["product_id"])
        warehouse = Warehouse.objects.get(id=self.validated_data["warehouse_id"])

        return services.stock_out(
            tenant=tenant,
            user=user,
            product=product,
            warehouse=warehouse,
            quantity=self.validated_data["quantity"],
            note=self.validated_data.get("note", ""),
        )
    

class StockAdjustSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    warehouse_id = serializers.IntegerField()
    new_quantity = serializers.DecimalField(max_digits=15, decimal_places=3)
    note = serializers.CharField(required=False, allow_blank=True)

    def save(self, **kwargs):
        request = self.context["request"]
        tenant = request.tenant
        user = request.user

        product = Product.objects.get(id=self.validated_data["product_id"])
        warehouse = Warehouse.objects.get(id=self.validated_data["warehouse_id"])

        return services.stock_adjust(
            tenant=tenant,
            user=user,
            product=product,
            warehouse=warehouse,
            quantity=self.validated_data["new_quantity"],
            note=self.validated_data.get("note", ""),
        )
    

class StockMovementSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    warehouse_name = serializers.CharField(source="warehouse.name")

    class Meta:
        model = StockMovement
        fields = [
            "id",
            "movement_type",
            "quantity",
            "product_name",
            "warehouse_name",
            "reference_type",
            "reference_id",
            "note",
            "created_at",
        ]
        read_only_fields = fields
