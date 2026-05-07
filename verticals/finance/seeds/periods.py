# verticals/finance/seeds/periods.py

from datetime import date
import calendar


def generate_year_periods(year: int):
    periods = []

    for month in range(1, 13):
        last_day = calendar.monthrange(year, month)[1]

        periods.append({
            "name": f"{calendar.month_abbr[month]} {year}",
            "start_date": date(year, month, 1),
            "end_date": date(year, month, last_day),
            "status": "open",
        })

    return periods


PERIODS = [
    *generate_year_periods(2026),
]