# core/dashboard/services.py

from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.contrib.auth import get_user_model
from business.products.models import Product  # contoh
from typing import Dict, Any

User = get_user_model()


class DashboardService:
    """
    Semua method:
    - static
    - read-only
    - permission-aware (via company / user)
    """

    @staticmethod
    def total_users(*, tenant, **kwargs) -> int:
        return User.objects.filter(
            tenant_memberships__tenant=tenant,
            tenant_memberships__is_active=True,
        ).count()


    @staticmethod
    def active_users(*, tenant, **kwargs) -> int:
        return User.objects.filter(
            tenant_memberships__tenant=tenant,
            tenant_memberships__is_active=True,
            is_active=True,
        ).count()


    @staticmethod
    def total_products(*, tenant, **kwargs) -> int:
        return Product.objects.filter(
            tenant=tenant, is_deleted=False
        ).count()


    @staticmethod
    def users_growth_by_month(*, tenant, **kwargs):
        qs = (
            User.objects
            .filter(
                tenant_memberships__tenant=tenant,
                tenant_memberships__is_active=True,
            )
            .annotate(month=TruncMonth("date_joined"))
            .values("month")
            .annotate(total=Count("id"))
            .order_by("month")
        )

        return {
            "labels": [row["month"].strftime("%b %Y") for row in qs],
            "datasets": [
                {
                    "label": "New Users",
                    "data": [row["total"] for row in qs],
                }
            ],
        }
    

    @staticmethod
    def recent_users(*, tenant, limit=5, **kwargs):
        qs = (
            User.objects
            .filter(
                tenant_memberships__tenant=tenant,
                tenant_memberships__is_active=True,
            )
            .order_by("-date_joined")[:limit]
        )

        return {
            "columns": [
                {"key": "username", "label": "Username"},
                {"key": "email", "label": "Email"},
                {"key": "is_active", "label": "Active"},
            ],
            "rows": [
                {
                    "id": u.id,
                    "username": u.username,
                    "email": u.email,
                    "is_active": u.is_active,
                }
                for u in qs
            ],
        }