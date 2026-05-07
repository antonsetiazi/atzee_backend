# accounting/entities/journal_create.py

from django.db import transaction
from core.entities.contracts import BaseEntity
from accounting.models import Journal, JournalEntry
from accounting.services.posting_service import PostingService
from accounting.enum.permissions import AccountingPermission


class JournalCreateEntity(BaseEntity):
    key = "accounting.journals.create"
    domain = "accounting"
    permission = AccountingPermission.JOURNAL_CREATE

    def query(self, *, user, tenant, query: dict):
        return {}
    
    @transaction.atomic
    def execute(self, *, user, tenant, data: dict):
        # 1. create journal header
        journal = Journal.objects.create(
            tenant=tenant,
            date=data["date"],
            reference=data.get("reference"),
            description=data.get("description"),
            created_by=user,
        )

        # 2. create lines
        for line in data["lines"]:
            JournalEntry.objects.create(
                tenant=tenant,
                journal=journal,
                account_id=line["account_id"],
                debit=line.get("debit", 0),
                credit=line.get("credit", 0),
                created_by=user,
            )

        # 3. posting
        PostingService.post_journal(journal)

        return {
            "success": True,
            "id": str(journal.id)
        }