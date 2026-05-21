# hrms/services/attendance/calculate_late_minutes.py

from datetime import datetime

DEFAULT_START_HOUR = 8
DEFAULT_START_MINUTE = 0


def calculate_late_minutes(
    attendance,
    start_hour=DEFAULT_START_HOUR,
    start_minute=DEFAULT_START_MINUTE,
):
    """
    Calculate employee lateness in minutes.
    """

    if not attendance.check_in:
        return 0

    expected_start = datetime.combine(
        attendance.attendance_date,
        datetime.min.time(),
    ).replace(
        hour=start_hour,
        minute=start_minute,
    )

    actual_check_in = attendance.check_in.replace(tzinfo=None)

    late_duration = actual_check_in - expected_start

    late_minutes = late_duration.total_seconds() / 60

    if late_minutes <= 0:
        return 0

    return int(late_minutes)
