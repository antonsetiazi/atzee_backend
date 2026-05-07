# verticals/finance/entities/admin_dashboard.py

from django.utils import timezone

from core.entities.contracts import BaseEntity
# from business.bookings.models import Booking, BookingStatus
from business.payments.models import Payment
from business.partners.models import Partner
from core.widgets import selectors

from verticals.finance.enum.permissions import FinancePermission

class AdminDashboardEntity(BaseEntity):
    """
    finance.admin.dashboard entity
    """

    key = "admin.dashboard"
    domain = "finance"
    permission = FinancePermission.ADMIN_DASHBOARD_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:
        now = timezone.now()

        try:
            # =====================================================
            # BASE QUERYSETS (TENANT LEVEL)
            # =====================================================
            # booking_qs = Booking.objects.filter(
            #     tenant=tenant,
            #     is_deleted=False,
            # )

            payment_qs = Payment.objects.filter(
                tenant=tenant,
                is_deleted=False,
            )

            partner_qs = Partner.objects.filter(
                tenant=tenant,
                is_deleted=False,
            )

            # =====================================================
            # PARTNER HEALTH
            # =====================================================
            active_partners = partner_qs.filter(
                is_active=True
            ).count()

            pending_verification = partner_qs.filter(
                is_active=False
            ).count()

            # Placeholder (until review/dispute entity added)
            flagged_reviews = 0
            open_disputes = 0

            # =====================================================
            # RECENT TRANSACTIONS (MAX 10)
            # =====================================================
            recent_tx_qs = payment_qs.order_by("-created_at")[:10]

            recent_transactions = [
                {
                    "id": str(p.id),
                    "transaction_number": p.transaction_number,
                    "user_name": str(p.user),
                    "amount": float(p.amount),
                    "status": p.status,
                }
                for p in recent_tx_qs
            ]

            # =====================================================
            # ALERT / BANNER SYSTEM
            # =====================================================
            widgets = selectors.get_active_widgets_for_user(
                tenant=tenant,
                user=user,
            )

            alerts = []

            for w in widgets:
                if w.type != "banner":
                    continue
                
                config = w.config or {}
                if isinstance(config, list):
                    config = config[0] if config else {}

                alerts.append({
                    "id": str(w.id),
                    "title": w.title,
                    "image_url": config.get("image_url"),
                    "link_url": config.get("link_url"),
                    "open_in_new_tab": config.get("open_in_new_tab", True),
                })

            # =====================================================
            # FINAL RESPONSE
            # =====================================================
            return {
                "active_partners": active_partners,
                "pending_verification": pending_verification,
                "flagged_reviews": flagged_reviews,
                "open_disputes": open_disputes,

                # "real_time_bookings": real_time_bookings,
                "recent_transactions": recent_transactions,

                "alerts": alerts,
            }

        except Exception as e:
            print(e)
            return {
                "today_bookings": 0,
                "active_bookings": 0,
                "completed_today": 0,
                "cancelled_today": 0,

                "platform_revenue": 0.0,
                "pending_payment": 0,
                "pending_payout": 0,
                "escrow_balance": 0.0,

                "active_partners": 0,
                "pending_verification": 0,
                "flagged_reviews": 0,
                "open_disputes": 0,

                "real_time_bookings": [],
                "recent_transactions": [],
                "alerts": None,
            }