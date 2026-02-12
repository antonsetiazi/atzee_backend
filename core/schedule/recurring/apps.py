# core/schedule/recurring/apps.py

from django.apps import AppConfig


class RecurringConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.schedule.recurring"
    label = "core_schedule_recurring"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.recurring_list import RecurringRuleListEntity
        from .entities.recurring_select_list import RecurringRuleSelectListEntity

        register_entity(RecurringRuleListEntity())
        register_entity(RecurringRuleSelectListEntity())
