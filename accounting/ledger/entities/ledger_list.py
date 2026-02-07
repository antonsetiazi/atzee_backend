from core.entities.contracts import BaseEntity
from accounting.ledger.models import LedgerEntry


class LedgerListEntity(BaseEntity):
    """
    ledger.list entity
    """

    key = "ledger.list"
    domain = "accounting"
    permission = "accounting.ledger.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format:
        {
            page: 1,
            pageSize: 20,
            filters?: {
                account?: str,
                date_from?: str,
                date_to?: str
            }
        }
        """

        qs = LedgerEntry.objects.filter(
            tenant=tenant
        ).select_related(
            "journal",
        )

        # 🔎 FILTERS
        filters = query.get("filters") or {}

        account = filters.get("account")
        if account:
            qs = qs.filter(account_code=account)

        date_from = filters.get("date_from")
        if date_from:
            qs = qs.filter(entry_date__gte=date_from)

        date_to = filters.get("date_to")
        if date_to:
            qs = qs.filter(entry_date__lte=date_to)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 20))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("entry_date", "id")[offset:limit]

        data = [
            {
                "id": str(e.id),
                "entry_date": e.entry_date,
                "account_code": e.account_code,
                "account_name": e.account_name,
                "debit": str(e.debit),
                "credit": str(e.credit),
                "journal_number": e.journal.journal_number,
            }
            for e in items
        ]

        return {
            "items": data,
            "total": total,
        }
