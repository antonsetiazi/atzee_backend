# verticals/pos/entities/cashier_sales.py

from django.utils import timezone
from django.db.models import Prefetch

from core.entities.contracts import BaseEntity

from business.products.models import Product, PartnerOffering
from core.schedule.shifts.models import Shift

from verticals.pos.enum.permissions import PosPermission


class CashierSalesEntity(BaseEntity):
    """
    pos.cashier.sales entity
    Used for POS transaction workspace
    """

    key = "cashier.sales"
    domain = "pos"
    permission = PosPermission.TRANSACTION_CASHIER_CREATE

    def query(self, *, user, tenant, query: dict) -> dict:
        now = timezone.now()

        try:
            # =====================================================
            # ACTIVE PARTNER PRODUCTS (POS SOURCE OF TRUTH)
            # =====================================================

            partner_products_qs = (
                PartnerOffering.objects
                .select_related("product")
                .filter(
                    tenant=tenant,
                    is_deleted=False,
                    is_active=True,
                )
                .order_by("product__name")
            )

            products = []

            for pp in partner_products_qs:
                products.append({
                    "id": str(pp.product.id),
                    "name": pp.product.name,
                    "price": float(pp.price),
                    "code": pp.product.code,
                    "product_type": pp.product.product_type,
                })

            # =====================================================
            # ACTIVE SHIFT
            # =====================================================

            active_shift = Shift.objects.filter(
                tenant=tenant,
                start_datetime__lte=now,
                end_datetime__gte=now,
                participants=user,
            ).order_by("-start_datetime").first()

            shift_data = None

            if active_shift:
                shift_data = {
                    "id": str(active_shift.id),
                    "start": active_shift.start_datetime,
                    "end": active_shift.end_datetime,
                }

            # =====================================================
            # RESPONSE
            # =====================================================

            return {
                "products": products,
                "active_shift": shift_data,
            }

        except Exception as e:
            print(e)
            return {
                "products": [],
                "active_shift": None,
            }