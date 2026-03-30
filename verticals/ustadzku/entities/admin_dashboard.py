# verticals/ustadzku/entities/admin_dashboard.py

from django.utils import timezone
from django.db import models
from django.db.models import Sum

from core.entities.contracts import BaseEntity
# from business.bookings.models import Booking, BookingStatus
from business.payments.models import Payment
from business.partners.models import Partner
from core.widgets.models import UIWidget

from verticals.ustadzku.enum.permissions import UstadzkuPermission

class AdminDashboardEntity(BaseEntity):
    """
    ustadzku.admin.dashboard entity
    """

    key = "admin.dashboard"
    domain = "ustadzku"
    permission = UstadzkuPermission.ADMIN_DASHBOARD_VIEW

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
            # BOOKING KPIs
            # =====================================================
            # today_bookings = booking_qs.filter(
            #     start_time__date=now.date()
            # ).count()

            # active_bookings = booking_qs.filter(
            #     status=BookingStatus.ON_GOING
            # ).count()

            # completed_today = booking_qs.filter(
            #     start_time__date=now.date(),
            #     status__in=[BookingStatus.COMPLETED, BookingStatus.SETTLED]
            # ).count()

            # cancelled_today = booking_qs.filter(
            #     start_time__date=now.date(),
            #     status=BookingStatus.CANCELLED
            # ).count()

            # =====================================================
            # FINANCIAL KPIs (BASED ON BOOKING STATUS)
            # =====================================================

            # Revenue Platform (Bulan Ini)
            # platform_revenue = (
            #     booking_qs.filter(
            #         status=BookingStatus.SETTLED,
            #         start_time__year=now.year,
            #         start_time__month=now.month,
            #     ).aggregate(total=Sum("platform_fee"))["total"]
            #     or 0
            # )

            # Booking yang belum dibayar
            # pending_payment = booking_qs.filter(
            #     status=BookingStatus.PENDING_PAYMENT
            # ).count()

            # Sudah selesai tapi belum settled ke partner
            # pending_payout = booking_qs.filter(
            #     status=BookingStatus.COMPLETED,
            #     is_financial_locked=True
            # ).count()

            # Escrow estimation:
            # Sudah CONFIRMED / ON_GOING tapi belum SETTLED
            # escrow_balance = (
            #     booking_qs.filter(
            #         status__in=[
            #             BookingStatus.CONFIRMED,
            #             BookingStatus.ON_GOING,
            #             BookingStatus.COMPLETED,
            #         ]
            #     ).exclude(
            #         status=BookingStatus.SETTLED
            #     ).aggregate(total=Sum("total_price"))["total"]
            #     or 0
            # )

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
            # REAL-TIME BOOKINGS (MAX 10)
            # =====================================================
            # realtime_qs = booking_qs.filter(
            #     status__in=[
            #         BookingStatus.CONFIRMED,
            #         BookingStatus.ON_GOING,
            #         BookingStatus.PENDING_PAYMENT,
            #     ]
            # ).order_by("-updated_at")[:10]

            # real_time_bookings = [
            #     {
            #         "id": str(b.id),
            #         "booking_number": b.booking_number,
            #         "partner_name": str(b.partner),
            #         "current_status": b.status,
            #         "status": b.status,
            #     }
            #     for b in realtime_qs
            # ]

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
            widget_qs = UIWidget.objects.filter(
                tenant=tenant,
                type="banner",
                is_deleted=False,
                is_active=True,
            ).filter(
                models.Q(starts_at__isnull=True) | models.Q(starts_at__lte=now)
            ).filter(
                models.Q(ends_at__isnull=True) | models.Q(ends_at__gte=now)
            ).order_by("order")

            alerts = []

            for w in widget_qs:
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
                # "today_bookings": today_bookings,
                # "active_bookings": active_bookings,
                # "completed_today": completed_today,
                # "cancelled_today": cancelled_today,

                # "platform_revenue": float(platform_revenue),
                # "pending_payment": pending_payment,
                # "pending_payout": pending_payout,
                # "escrow_balance": float(escrow_balance),

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