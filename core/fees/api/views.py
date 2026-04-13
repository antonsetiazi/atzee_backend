# core/fees/api/views.py

from rest_framework.viewsets import ModelViewSet
from core.fees.models import FeeConfig
from .serializers import FeeConfigSerializer


class FeeConfigViewSet(ModelViewSet):
    queryset = FeeConfig.objects.all()
    serializer_class = FeeConfigSerializer