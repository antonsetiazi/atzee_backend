# core/schedule/events/apps.py

from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.schedule.events"
    label = "core_schedule_events"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.event_list import EventListEntity
        from .entities.event_select_list import EventSelectListEntity

        register_entity(EventListEntity())
        register_entity(EventSelectListEntity())
