# core/lookups/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import LookupService


class LookupView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, key: str):
        try:
            result = LookupService.execute(key)
            return Response(result)
        except ValueError:
            return Response(
                {"detail": "Lookup not found"},
                status=404,
            )
