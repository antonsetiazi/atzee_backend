# accounting/api/taxes/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.tenants.services import TenantService
from accounting.models import Tax

from .serializers import (
    TaxSerializer
)


class TaxListAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        qs = Tax.objects.filter(
            tenant=tenant
        )

        data = TaxSerializer(
            qs,
            many=True
        ).data

        return Response(data)


class TaxCreateAPIView(APIView):

    def post(self, request):
        tenant = TenantService.get_current_tenant(request)
        
        serializer = TaxSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        obj = serializer.save(
            tenant=tenant,
            created_by=request.user,
        )

        return Response(
            TaxSerializer(obj).data,
            status=status.HTTP_201_CREATED
        )