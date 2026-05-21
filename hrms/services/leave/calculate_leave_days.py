# hrms/services/leave/calculate_leave_days.py

# from datetime import timedelta


def calculate_leave_days(
    start_date,
    end_date,
):
    """
    Calculate total leave days.
    """

    duration = end_date - start_date

    return duration.days + 1
