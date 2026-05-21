# hrms/services/attendance/calculate_work_hours.py

# from datetime import timedelta


def calculate_work_hours(attendance):
    """
    Calculate total worked hours.
    """

    if not attendance.check_in:
        return 0

    if not attendance.check_out:
        return 0

    duration = attendance.check_out - attendance.check_in

    hours = duration.total_seconds() / 3600

    return round(hours, 2)
