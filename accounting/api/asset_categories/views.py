# accounting/api/asset_categories/views.py

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import (
    Account,
    AssetCategory,
)
from core.tenants.services import TenantService

from .serializers import (
    AssetCategoryCreateSerializer,
    AssetCategoryReadSerializer,
)


class AssetCategoryListAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        qs = AssetCategory.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        search = request.GET.get("search")

        if search:
            qs = qs.filter(name__icontains=search)

        qs = qs.order_by("code")

        data = AssetCategoryReadSerializer(
            qs,
            many=True,
        ).data

        return Response(data)


class AssetCategoryCreateAPIView(APIView):

    def post(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = AssetCategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated = serializer.validated_data

        asset_account = Account.objects.get(
            tenant=tenant,
            id=validated["asset_account_id"],
        )

        accumulated_account = Account.objects.get(
            tenant=tenant,
            id=validated["accumulated_depreciation_account_id"],
        )

        expense_account = Account.objects.get(
            tenant=tenant,
            id=validated["depreciation_expense_account_id"],
        )

        category = AssetCategory.objects.create(
            tenant=tenant,
            code=validated["code"],
            name=validated["name"],
            description=validated.get("description", ""),
            asset_account=asset_account,
            accumulated_depreciation_account=accumulated_account,
            depreciation_expense_account=expense_account,
            depreciation_method=validated["depreciation_method"],
            useful_life_months=validated["useful_life_months"],
            salvage_value_percent=validated.get("salvage_value_percent", 0),
            created_by=request.user,
        )

        return Response(
            AssetCategoryReadSerializer(category).data,
            status=status.HTTP_201_CREATED,
        )


class AssetCategoryDetailAPIView(APIView):

    def get_object(self, tenant, category_id):
        return get_object_or_404(
            AssetCategory,
            id=category_id,
            tenant=tenant,
            is_deleted=False,
        )

    def get(self, request, category_id):
        tenant = TenantService.get_current_tenant(request)

        category = self.get_object(tenant, category_id)
        data = AssetCategoryReadSerializer(category).data

        return Response(data)

    def put(self, request, category_id):
        tenant = TenantService.get_current_tenant(request)

        category = self.get_object(tenant, category_id)

        serializer = AssetCategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated = serializer.validated_data

        category.code = validated["code"]
        category.name = validated["name"]
        category.description = validated.get("description", "")

        # FIX IMPORTANT: pakai object, bukan *_id langsung
        category.asset_account = Account.objects.get(
            tenant=tenant,
            id=validated["asset_account_id"],
        )

        category.accumulated_depreciation_account = Account.objects.get(
            tenant=tenant,
            id=validated["accumulated_depreciation_account_id"],
        )

        category.depreciation_expense_account = Account.objects.get(
            tenant=tenant,
            id=validated["depreciation_expense_account_id"],
        )

        category.depreciation_method = validated["depreciation_method"]
        category.useful_life_months = validated["useful_life_months"]
        category.salvage_value_percent = validated.get(
            "salvage_value_percent", 0
        )

        category.updated_by = request.user
        category.save()

        return Response(AssetCategoryReadSerializer(category).data)

    def delete(self, request, category_id):
        tenant = TenantService.get_current_tenant(request)

        category = self.get_object(tenant, category_id)
        category.is_deleted = True
        category.updated_by = request.user
        category.save()

        return Response({"success": True})
