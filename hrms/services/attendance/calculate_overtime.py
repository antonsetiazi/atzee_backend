# hrms/services/attendance/calculate_overtime.py

from datetime import timedelta

DEFAULT_WORK_HOURS = 8


def calculate_overtime(
    attendance,
    standard_work_hours=DEFAULT_WORK_HOURS,
):
    """
    Calculate employee overtime hours.
    """

    if not attendance.check_in:
        return 0

    if not attendance.check_out:
        return 0

    worked_duration = attendance.check_out - attendance.check_in

    standard_duration = timedelta(hours=standard_work_hours)

    overtime_duration = worked_duration - standard_duration

    if overtime_duration.total_seconds() <= 0:
        return 0

    overtime_hours = overtime_duration.total_seconds() / 3600

    return round(overtime_hours, 2)
