# core/activity/events/system_events.py

"""
System activity event definitions.
"""

from core.activity.constants.events import (
    SYSTEM_ROLE_UPDATED,
    SYSTEM_SETTING_UPDATED,
    SYSTEM_USER_CREATED,
    SYSTEM_USER_LOGIN,
    SYSTEM_USER_LOGOUT,
)


class SystemEvents:

    USER_LOGIN = SYSTEM_USER_LOGIN

    USER_LOGOUT = SYSTEM_USER_LOGOUT

    USER_CREATED = SYSTEM_USER_CREATED

    ROLE_UPDATED = SYSTEM_ROLE_UPDATED

    SETTING_UPDATED = SYSTEM_SETTING_UPDATED
