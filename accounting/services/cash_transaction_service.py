# accounting/services/cash_transaction_service.py

from django.db import transaction

from accounting.models import (
    CashTransaction,
    CashBankAccount,
)

from accounting.services.cash_bank_service import (
    CashBankService
)

from accounting.services.auto_journal_service import (
    AutoJournalService
)


class CashTransactionService:

    @staticmethod
    @transaction.atomic
    def create_cash_in(
        *,
        tenant,
        user,
        transaction_number,
        transaction_date,
        to_account_id,
        amount,
        reference="",
        description=""
    ):

        to_account = (
            CashBankAccount.objects.get(
                id=to_account_id,
                tenant=tenant
            )
        )

        trx = CashTransaction.objects.create(
            tenant=tenant,
            transaction_number=transaction_number,
            transaction_type="cash_in",
            transaction_date=transaction_date,
            to_account=to_account,
            amount=amount,
            reference=reference,
            description=description,
            created_by=user,
        )

        CashBankService.increase_balance(
            to_account,
            amount
        )

        AutoJournalService.create_from_transaction(
            tenant=tenant,
            user=user,
            transaction_type="payment_in",
            reference=trx.transaction_number,
            date=trx.transaction_date,
            payload={
                "total_amount": trx.amount
            }
        )

        return trx


    @staticmethod
    @transaction.atomic
    def create_cash_out(
        *,
        tenant,
        user,
        transaction_number,
        transaction_date,
        from_account_id,
        amount,
        reference="",
        description=""
    ):

        from_account = (
            CashBankAccount.objects.get(
                id=from_account_id,
                tenant=tenant
            )
        )

        trx = CashTransaction.objects.create(
            tenant=tenant,
            transaction_number=transaction_number,
            transaction_type="cash_out",
            transaction_date=transaction_date,
            from_account=from_account,
            amount=amount,
            reference=reference,
            description=description,
            created_by=user,
        )

        CashBankService.decrease_balance(
            from_account,
            amount
        )

        AutoJournalService.create_from_transaction(
            tenant=tenant,
            user=user,
            transaction_type="payment_out",
            reference=trx.transaction_number,
            date=trx.transaction_date,
            payload={
                "total_amount": trx.amount
            }
        )

        return trx


    @staticmethod
    @transaction.atomic
    def create_transfer(
        *,
        tenant,
        user,
        transaction_number,
        transaction_date,
        from_account_id,
        to_account_id,
        amount,
        reference="",
        description=""
    ):

        if from_account_id == to_account_id:

            raise ValueError(
                "Cannot transfer to same account"
            )

        from_account = (
            CashBankAccount.objects.get(
                id=from_account_id,
                tenant=tenant
            )
        )

        to_account = (
            CashBankAccount.objects.get(
                id=to_account_id,
                tenant=tenant
            )
        )

        trx = CashTransaction.objects.create(
            tenant=tenant,
            transaction_number=transaction_number,
            transaction_type="transfer",
            transaction_date=transaction_date,
            from_account=from_account,
            to_account=to_account,
            amount=amount,
            reference=reference,
            description=description,
            created_by=user,
        )

        CashBankService.decrease_balance(
            from_account,
            amount
        )

        CashBankService.increase_balance(
            to_account,
            amount
        )

        return trx