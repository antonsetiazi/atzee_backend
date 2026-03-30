# business/booking/services/availability.py

from datetime import datetime, time, timedelta
from django.utils import timezone
from django.db.models import Q

from business.booking.models import Booking, BookingStatus
from business.partners.models import Partner


# 🔥 Booking yang dianggap "blocking"
ACTIVE_BOOKING_FILTER = Q(
    status__in=[
        BookingStatus.CONFIRMED,
        BookingStatus.ONGOING,
    ]
) | Q(
    status=BookingStatus.HOLD,
    expires_at__gt=timezone.now()
)


# =========================================================
# 🧠 HELPER: Get Partner Working Hours
# =========================================================
def get_partner_working_hours(partner):
    """
    Return (start_hour, end_hour) untuk partner.

    Priority:
    1. PartnerServiceProfile.working_hours
    2. Default (8, 18)
    """

    service_profile = getattr(partner, "service_profile", None)

    if service_profile and service_profile.working_hours:
        wh = service_profile.working_hours

        return (
            int(wh.get("start", 8)),
            int(wh.get("end", 18)),
        )

    return (8, 18)


# =========================================================
# 🧠 HELPER: Generate Start Times
# =========================================================
def generate_start_times(start, end, step_minutes=30):
    """
    Generate possible START times (bukan slot range lagi)
    """
    current = start
    delta = timedelta(minutes=step_minutes)

    while current < end:
        yield current
        current += delta


# =========================================================
# 🧠 HELPER: Check Range Availability
# =========================================================
def is_range_available(start, end, booking_ranges):
    """
    Check apakah range (start → end) bentrok dengan booking lain
    """
    for b_start, b_end in booking_ranges:
        if b_start < end and b_end > start:
            return False
    return True


# =========================================================
# 🚀 MAIN FUNCTION
# =========================================================
def get_availability(
    *,
    tenant,
    resource_type: str,
    resource_id,
    date,
    duration_minutes: int,
    step_minutes=30,
):
    """
    SESSION-BASED AVAILABILITY ENGINE

    Return list of AVAILABLE START TIMES untuk durasi tertentu

    Contoh:
    duration = 120 menit

    Output:
    [
        {start_time: 10:00, end_time: 12:00, is_available: True},
        {start_time: 10:30, end_time: 12:30, is_available: False},
        ...
    ]
    """

    # 🔥 Validasi basic
    if duration_minutes <= 0:
        raise ValueError("duration_minutes must be greater than 0")

    try:
        # =====================================================
        # 🧠 Ambil Partner (resource)
        # =====================================================
        partner = Partner.objects.get(
            id=resource_id,
            tenant=tenant
        )

        start_hour, end_hour = get_partner_working_hours(partner)

        # =====================================================
        # 🧠 Setup waktu harian (timezone-aware)
        # =====================================================
        tz = timezone.get_current_timezone()

        start_of_day = datetime.combine(date, time.min)
        start_of_day = timezone.make_aware(start_of_day, tz)

        day_start = start_of_day.replace(hour=start_hour, minute=0)
        day_end = start_of_day.replace(hour=end_hour, minute=0)

        duration_delta = timedelta(minutes=duration_minutes)

        # =====================================================
        # 🧠 Ambil booking existing (blocking only)
        # =====================================================
        bookings = (
            Booking.objects
            .filter(
                tenant=tenant,
                resource_type=resource_type,
                resource_id=resource_id,
                start_time__lt=day_end,
                end_time__gt=day_start,
            )
            .filter(ACTIVE_BOOKING_FILTER)
            .values("start_time", "end_time")
        )

        booking_ranges = [
            (b["start_time"], b["end_time"])
            for b in bookings
        ]

        results = []

        # =====================================================
        # 🚀 Generate possible START TIMES
        # =====================================================
        for start_time in generate_start_times(day_start, day_end, step_minutes):

            end_time = start_time + duration_delta

            # ❗ Skip kalau melewati jam kerja
            if end_time > day_end:
                continue

            is_available = is_range_available(
                start_time,
                end_time,
                booking_ranges
            )

            results.append({
                "start_time": start_time,
                "end_time": end_time,
                "is_available": is_available,
            })

        return results

    except Partner.DoesNotExist:
        return []

    except Exception as e:
        print("Availability error:", e)
        return []