# accounting/journals/entities/journal_list.py

from django.db.models import Sum
from core.entities.contracts import BaseEntity
from accounting.journals.models import Journal
from accounting.journals.constants import JournalStatus


class JournalListEntity(BaseEntity):
    """
    journals.list entity
    """

    key = "journals.list"
    domain = "accounting"
    permission = "accounting.journals.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        query format (from frontend):
        {
            page: 1,
            pageSize: 10,
            search?: str,
            filters?: {
                status?: str,
                journal_type?: str,
                date_from?: str,
                date_to?: str,
            }
        }
        """
        try:

            qs = (
                Journal.objects
                .filter(
                    tenant=tenant,
                    status__in=[
                        JournalStatus.DRAFT,
                        JournalStatus.POSTED,
                    ],
                )
                .annotate(
                    total_debit=Sum("lines__debit"),
                    total_credit=Sum("lines__credit"),
                )
                .order_by("-journal_date", "-created_at")
            )

            # 🔍 SEARCH (journal number / description)
            search = query.get("search")
            if search:
                qs = qs.filter(
                    journal_number__icontains=search
                )

            # 🎛️ FILTERS
            filters = query.get("filters") or {}

            if status := filters.get("status"):
                qs = qs.filter(status=status)

            if journal_type := filters.get("journal_type"):
                qs = qs.filter(journal_type=journal_type)

            if date_from := filters.get("date_from"):
                qs = qs.filter(journal_date__gte=date_from)

            if date_to := filters.get("date_to"):
                qs = qs.filter(journal_date__lte=date_to)

            # 📄 PAGINATION
            page = int(query.get("page", 1))
            page_size = int(query.get("pageSize", 10))

            offset = (page - 1) * page_size
            limit = offset + page_size

            total = qs.count()
            items = qs[offset:limit]

            # 🔁 SERIALIZE (explicit, accounting-safe)
            data = [
                {
                    "id": str(j.id),
                    "journal_number": j.journal_number,
                    "journal_date": j.journal_date,
                    "journal_type": j.journal_type,
                    "status": j.status,
                    "description": j.description,
                    "total_debit": j.total_debit or 0,
                    "total_credit": j.total_credit or 0,
                }
                for j in items
            ]

            return {
                "items": data,
                "total": total,
            }
        
        except Exception as e:
            print(e)
