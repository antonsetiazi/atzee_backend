# accounting/services/posting_service.py

from decimal import Decimal
from django.utils import timezone
from django.db import transaction
from accounting.models import AccountLedger
from accounting.services.period_service import PeriodService


class PostingService:

    @staticmethod
    def validate_balance(entries):
        total_debit = sum([e.debit for e in entries])
        total_credit = sum([e.credit for e in entries])

        if total_debit != total_credit:
            raise ValueError(
                f"Unbalanced Journal: Debit={total_debit} Credit={total_credit}"
            )


    @staticmethod
    def validate_tenant(journal, entries):
        for e in entries:
            if e.tenant_id != journal.tenant_id:
                raise ValueError("Tenant mismatch in journal entries")


    @staticmethod
    def validate_accounts(entries):
        for e in entries:
            acc = e.account

            if acc.is_group:
                raise ValueError(f"Account {acc.code} is a group account")

            if not acc.is_active:
                raise ValueError(f"Account {acc.code} is inactive")


    @staticmethod
    def get_last_balance(account, tenant):
        last = AccountLedger.objects.filter(
            account=account,
            tenant=tenant
        ).order_by("-date", "-created_at").first()

        return last.balance if last else Decimal("0")
      

    @staticmethod
    def create_ledger_entries(journal, entries):
        ledger_objects = []

        # 🔥 cache running balance per account
        balance_map = {}

        for e in entries:
            key = str(e.account_id)

            if key not in balance_map:
                balance_map[key] = PostingService.get_last_balance(
                    e.account,
                    e.tenant
                )

            new_balance = balance_map[key] + e.debit - e.credit

            balance_map[key] = new_balance

            ledger_objects.append(
                AccountLedger(
                    tenant=e.tenant,
                    journal=journal,
                    entry=e,
                    account=e.account,
                    date=journal.date,
                    debit=e.debit,
                    credit=e.credit,
                    balance=new_balance
                )
            )

        AccountLedger.objects.bulk_create(ledger_objects)


    @staticmethod
    @transaction.atomic
    def post_journal(journal):
        if journal.is_posted:
            raise ValueError("Journal already posted")

        entries = list(journal.entries.all())

        if not entries:
            raise ValueError("Journal has no entries")

        PostingService.validate_tenant(journal, entries)
        PostingService.validate_balance(entries)
        PostingService.validate_accounts(entries)

        # VALIDASI PERIOD
        PeriodService.validate_posting_allowed(
            tenant=journal.tenant,
            date=journal.date
        )

        PostingService.create_ledger_entries(journal, entries)

        # MARK POSTED
        journal.is_posted = True
        journal.posted_at = timezone.now()
        journal.save()

        return journal