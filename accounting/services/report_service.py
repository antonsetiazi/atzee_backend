# accounting/services/report_service.py

from django.db.models import Sum
from accounting.models import AccountLedger, Account


class ReportService:

    @staticmethod
    def get_trial_balance(tenant, date_from=None, date_to=None):
        """
        Menghasilkan trial balance per akun
        """

        qs = AccountLedger.objects.filter(
            tenant=tenant
        )

        if date_from:
            qs = qs.filter(date__gte=date_from)

        if date_to:
            qs = qs.filter(date__lte=date_to)

        # group by account
        grouped = qs.values("account").annotate(
            total_debit=Sum("debit"),
            total_credit=Sum("credit")
        )

        result = []
        total_debit = 0
        total_credit = 0

        account_map = {
            acc.id: acc for acc in Account.objects.filter(tenant=tenant)
        }

        for row in grouped:
            account = account_map.get(row["account"])
            if not account:
                continue

            debit = row["total_debit"] or 0
            credit = row["total_credit"] or 0

            balance = debit - credit

            result.append({
                "account_id": str(account.id),
                "code": account.code,
                "name": account.name,
                "debit": debit,
                "credit": credit,
                "balance": balance
            })

            total_debit += debit
            total_credit += credit

        return {
            "accounts": result,
            "total_debit": total_debit,
            "total_credit": total_credit
        }
    

    @staticmethod
    def get_profit_loss(tenant, date_from=None, date_to=None):
        qs = AccountLedger.objects.filter(tenant=tenant)

        if date_from:
            qs = qs.filter(date__gte=date_from)

        if date_to:
            qs = qs.filter(date__lte=date_to)

        # hanya revenue & expense
        accounts = Account.objects.filter(
            tenant=tenant,
            account_type__in=["revenue", "expense"],
            is_group=False
        )

        account_map = {acc.id: acc for acc in accounts}

        grouped = qs.values("account").annotate(
            total_debit=Sum("debit"),
            total_credit=Sum("credit")
        )

        revenues = []
        expenses = []

        total_revenue = 0
        total_expense = 0

        for row in grouped:
            acc = account_map.get(row["account"])
            if not acc:
                continue

            debit = row["total_debit"] or 0
            credit = row["total_credit"] or 0

            # gunakan normal balance
            if acc.normal_balance == "credit":
                balance = credit - debit
            else:
                balance = debit - credit

            item = {
                "account_id": str(acc.id),
                "code": acc.code,
                "name": acc.name,
                "amount": balance
            }

            if acc.account_type == "revenue":
                revenues.append(item)
                total_revenue += balance
            elif acc.account_type == "expense":
                expenses.append(item)
                total_expense += balance

        net_profit = total_revenue - total_expense

        return {
            "revenues": revenues,
            "expenses": expenses,
            "total_revenue": total_revenue,
            "total_expense": total_expense,
            "net_profit": net_profit
        }
    

    @staticmethod
    def get_balance_sheet(tenant, date_to=None):
        qs = AccountLedger.objects.filter(tenant=tenant)

        if date_to:
            qs = qs.filter(date__lte=date_to)

        accounts = Account.objects.filter(
            tenant=tenant,
            account_type__in=["asset", "liability", "equity"],
            is_group=False
        )

        account_map = {acc.id: acc for acc in accounts}

        grouped = qs.values("account").annotate(
            total_debit=Sum("debit"),
            total_credit=Sum("credit")
        )

        assets = []
        liabilities = []
        equity = []

        total_assets = 0
        total_liabilities = 0
        total_equity = 0

        for row in grouped:
            acc = account_map.get(row["account"])
            if not acc:
                continue

            debit = row["total_debit"] or 0
            credit = row["total_credit"] or 0

            # gunakan normal balance
            if acc.normal_balance == "debit":
                balance = debit - credit
            else:
                balance = credit - debit

            item = {
                "account_id": str(acc.id),
                "code": acc.code,
                "name": acc.name,
                "balance": balance
            }

            if acc.account_type == "asset":
                assets.append(item)
                total_assets += balance

            elif acc.account_type == "liability":
                liabilities.append(item)
                total_liabilities += balance

            elif acc.account_type == "equity":
                equity.append(item)
                total_equity += balance

        return {
            "assets": assets,
            "liabilities": liabilities,
            "equity": equity,
            "total_assets": total_assets,
            "total_liabilities": total_liabilities,
            "total_equity": total_equity,
            "is_balanced": total_assets == (total_liabilities + total_equity)
        }