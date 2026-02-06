# business/inventory/serializers.py

from decimal import Decimal

from rest_framework import serializers

from business.inventory import services, selectors
from business.inventory.models.warehouse import Warehouse
from business.inventory.models.stock_item import StockItem
from business.inventory.models.stock_movement import StockMovement
from business.inventory.models.lot import InventoryLot
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


class StockMovementWithLotSerializer(StockMovementBaseSerializer):
    lot_id = serializers.IntegerField(required=False, allow_null=True)


class InventoryLotSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    warehouse_name = serializers.CharField(source="warehouse.name", read_only=True)

    class Meta:
        model = InventoryLot
        fields = [
            "id",
            "product_id",
            "product_name",
            "warehouse_id",
            "warehouse_name",
            "batch_code",
            "expiry_date",
            "quantity",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields


class InventoryLotCreateUpdateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    warehouse_id = serializers.IntegerField()
    batch_code = serializers.CharField(max_length=50)
    expiry_date = serializers.DateField()
    quantity = serializers.DecimalField(max_digits=15, decimal_places=3)

    def save(self, **kwargs) -> InventoryLot:
        request = self.context["request"]
        tenant = request.tenant
        user = request.user

        product = Product.objects.get(
            tenant=tenant,
            id=self.validated_data["product_id"]
        )

        warehouse = Warehouse.objects.get(
            tenant=tenant,
            id=self.validated_data["warehouse_id"]
        )

        lot = InventoryLot.objects.create(
            tenant=tenant,
            product=product,
            warehouse=warehouse,
            batch_code=self.validated_data["batch_code"],
            expiry_date=self.validated_data["expiry_date"],
            quantity=self.validated_data["quantity"],
            created_by=user,
            updated_by=user,
        )

        return lot
