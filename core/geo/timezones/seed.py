# core/geo/timezones/seed.py

from core.geo.timezones.models import Timezone


DEFAULT_TIMEZONES = [
    {"name": "UTC", "utc_offset": "+00:00"},
    {"name": "Asia/Jakarta", "utc_offset": "+07:00"},
    {"name": "Asia/Singapore", "utc_offset": "+08:00"},
    {"name": "Asia/Tokyo", "utc_offset": "+09:00"},
    {"name": "Asia/Shanghai", "utc_offset": "+08:00"},
    {"name": "Asia/Kuala_Lumpur", "utc_offset": "+08:00"},
    {"name": "Europe/London", "utc_offset": "+00:00"},
    {"name": "Europe/Berlin", "utc_offset": "+01:00"},
    {"name": "America/New_York", "utc_offset": "-05:00"},
    {"name": "America/Los_Angeles", "utc_offset": "-08:00"},
]


def seed_timezones(tenant):
    for tz in DEFAULT_TIMEZONES:
        Timezone.objects.update_or_create(
            tenant=tenant,
            name=tz["name"],
            defaults={
                "utc_offset": tz["utc_offset"],
                "is_active": True,
            },
        )
