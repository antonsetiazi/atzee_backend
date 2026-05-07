# accounting/services/period_service.py

from accounting.models import AccountingPeriod


class PeriodService:

    @staticmethod
    def get_period_for_date(tenant, date):
        return AccountingPeriod.objects.filter(
            tenant=tenant,
            start_date__lte=date,
            end_date__gte=date
        ).first()

    @staticmethod
    def validate_posting_allowed(tenant, date):
        period = PeriodService.get_period_for_date(tenant, date)

        if not period:
            raise ValueError("No accounting period found for this date")

        if period.is_locked:
            raise ValueError("Period is locked")

        if period.is_closed:
            raise ValueError("Period is closed")

        return period