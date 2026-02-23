# business/partners/availability.py

from datetime import datetime, time, timedelta
from typing import List, Dict
from django.utils import timezone

from business.partners.models import Partner


DEFAULT_OPEN_TIME = time(9, 0)   # 09:00
DEFAULT_CLOSE_TIME = time(17, 0) # 17:00
DEFAULT_SLOT_MINUTES = 60


def _round_to_hour(dt: datetime) -> datetime:
    """
    Normalize datetime to remove seconds & microseconds.
    """
    return dt.replace(minute=0, second=0, microsecond=0)


def generate_partner_daily_slots(
    *,
    partner: Partner,
    target_date: datetime,
    slot_minutes: int = DEFAULT_SLOT_MINUTES,
    open_time: time = DEFAULT_OPEN_TIME,
    close_time: time = DEFAULT_CLOSE_TIME,
    hide_past_slots: bool = True,
) -> List[Dict]:
    """
    Generate clean availability slots for a partner on specific date.

    This function:
    - Creates clean hour-based slots
    - Removes seconds/microseconds
    - Filters past slots (if today)
    - Returns standardized format for frontend
    """

    tz = timezone.get_current_timezone()
    now = timezone.now().astimezone(tz)

    # Normalize target_date to local midnight
    target_date = target_date.astimezone(tz)
    base_date = target_date.date()

    start_datetime = timezone.make_aware(
        datetime.combine(base_date, open_time),
        tz
    )

    end_datetime = timezone.make_aware(
        datetime.combine(base_date, close_time),
        tz
    )

    slots = []
    current = start_datetime

    while current < end_datetime:
        slot_end = current + timedelta(minutes=slot_minutes)

        available = True

        # 🔹 Hide past slots if today
        if hide_past_slots and base_date == now.date():
            if current <= now:
                available = False

        # TODO:
        # Here you will later check booking overlap
        # Example:
        # if booking_exists(partner, current, slot_end):
        #     available = False

        slots.append({
            "datetime": current.replace(second=0, microsecond=0).isoformat(),
            "available": available
        })

        current += timedelta(minutes=slot_minutes)

    return slots