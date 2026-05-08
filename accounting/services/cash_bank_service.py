# accounting/services/cash_bank_service.py

from decimal import Decimal

from accounting.models import (
    CashBankAccount
)


class CashBankService:

    @staticmethod
    def increase_balance(
        account,
        amount
    ):

        account.current_balance += Decimal(
            amount
        )

        account.save(
            update_fields=[
                "current_balance"
            ]
        )

        return account


    @staticmethod
    def decrease_balance(
        account,
        amount
    ):

        amount = Decimal(amount)

        if account.current_balance < amount:

            raise ValueError(
                f"Insufficient balance on "
                f"{account.name}"
            )

        account.current_balance -= amount

        account.save(
            update_fields=[
                "current_balance"
            ]
        )

        return account