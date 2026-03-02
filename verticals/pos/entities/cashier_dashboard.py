# verticals/pos/entities/cashier_dashboard.py

from django.utils import timezone
from django.db.models import Sum

from core.entities.contracts import BaseEntity

from business.transactions.models.transaction import Transaction
from business.transactions.models.transaction_item import TransactionItem
from business.transactions.models.enums import (
    TransactionType,
    TransactionStatus,
)

from core.schedule.shifts.models import Shift

from verticals.pos.enum.permissions import PosPermission


class CashierDashboardEntity(BaseEntity):
    """
    pos.cashier.dashboard entity
    """

    key = "cashier.dashboard"
    domain = "pos"
    permission = PosPermission.CASHIER_DASHBOARD_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:
        now = timezone.now()

        try:
            # =====================================================
            # BASE QUERYSET (SALES ONLY)
            # =====================================================

            tx_qs = Transaction.objects.filter(
                tenant=tenant,
                is_deleted=False,
                transaction_type=TransactionType.SALES,
                created_by=user,  # personal cashier
            )

            today_qs = tx_qs.filter(
                transaction_date=now.date(),
                status=TransactionStatus.COMPLETED,
            )

            # =====================================================
            # KPI
            # =====================================================

            # Total Sales Today
            today_sales = (
                TransactionItem.objects.filter(
                    tenant=tenant,
                    transaction__in=today_qs,
                ).aggregate(total=Sum("total_price"))["total"]
                or 0
            )

            # Total Transactions Today
            today_transactions = today_qs.count()

            # Total Items Sold Today
            items_sold = (
                TransactionItem.objects.filter(
                    tenant=tenant,
                    transaction__in=today_qs,
                ).aggregate(total=Sum("quantity"))["total"]
                or 0
            )

            # =====================================================
            # ACTIVE SHIFT (SCHEDULE BASED)
            # =====================================================

            active_shift = Shift.objects.filter(
                tenant=tenant,
                start_datetime__lte=now,
                end_datetime__gte=now,
                participants=user,
            ).order_by("-start_datetime").first()

            shift_balance = 0

            if active_shift:
                # optional: kalau mau ambil opening cash dari metadata
                opening_cash = 0

                if active_shift.metadata:
                    opening_cash = active_shift.metadata.get("opening_cash", 0)

                shift_balance = float(today_sales) + float(opening_cash)

            # =====================================================
            # RECENT PERSONAL TRANSACTIONS
            # =====================================================

            recent_qs = tx_qs.order_by("-transaction_date")[:10]

            recent_transactions = []

            for tx in recent_qs:

                total_amount = (
                    tx.items.aggregate(total=Sum("total_price"))["total"]
                    or 0
                )

                recent_transactions.append({
                    "id": str(tx.id),
                    "receipt_number": tx.reference,
                    "total_amount": float(total_amount),
                    "payment_method": tx.subtype or "-",  # sementara pakai subtype
                    "status": tx.status,
                })

            # =====================================================
            # RESPONSE
            # =====================================================

            return {
                "today_sales": float(today_sales),
                "today_transactions": today_transactions,
                "items_sold": float(items_sold),
                "shift_balance": float(shift_balance),
                "recent_transactions": recent_transactions,
            }

        except Exception as e:
            print(e)
            return {
                "today_sales": 0.0,
                "today_transactions": 0,
                "items_sold": 0,
                "shift_balance": 0.0,
                "recent_transactions": [],
            }