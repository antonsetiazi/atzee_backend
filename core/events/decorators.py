# core/events/decorators.py

from core.events.bus import register_event_listener


def event_listener(event_name: str):
    def decorator(func):
        register_event_listener(event_name, func)
        return func
    return decorator
