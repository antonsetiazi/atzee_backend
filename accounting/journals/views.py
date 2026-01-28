from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounting.journals import selectors
from accounting.journals.serializers import (
    JournalListSerializer,
    JournalDetailSerializer,
)
from accounting.journals.services import reverse_journal


class JournalViewSet(viewsets.ViewSet):
    """
    Accounting Journal API (read-only + reverse).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        journals = selectors.get_journal_queryset(
            tenant=request.tenant
        )

        serializer = JournalListSerializer(journals, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        journal = selectors.get_journal_by_id(
            tenant=request.tenant,
            journal_id=pk
        )

        if not journal:
            return Response(
                {"detail": "Journal not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = JournalDetailSerializer(journal)
        return Response(serializer.data)
    

    @action(detail=True, methods=["post"], url_path="reverse")
    def reverse(self, request, pk=None):
        journal = selectors.get_journal_by_id(
            tenant=request.tenant,
            journal_id=pk
        )

        if not journal:
            return Response(
                {"detail": "Journal not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        reversal = reverse_journal(
            journal=journal,
            reversed_by=request.user,
            reversal_date=request.data.get("reversal_date"),
            reason=request.data.get("reason", "")
        )

        serializer = JournalDetailSerializer(reversal)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )