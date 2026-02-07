from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from accounting.ledger.models import LedgerEntry
from accounting.ledger.serializers import LedgerEntrySerializer
from accounting.ledger.selectors import ledger_entries_qs
from core.permissions.access.accounting import IsAccountingViewer


class LedgerEntryViewSet(ReadOnlyModelViewSet):
    """
    Ledger is read-only.
    Source of truth = Journal → LedgerEntry
    """

    serializer_class = LedgerEntrySerializer
    permission_classes = [
        IsAuthenticated,
        IsAccountingViewer,
    ]

    def get_queryset(self):
        return ledger_entries_qs(
            tenant=self.request.user.tenant
        )
