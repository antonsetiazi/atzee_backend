# core/schedule/reminders/apps.py

from django.apps import AppConfig


class RemindersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.schedule.reminders"
    label = "core_schedule_reminders"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.reminder_list import ReminderListEntity
        from .entities.reminder_select_list import ReminderSelectListEntity

        register_entity(ReminderListEntity())
        register_entity(ReminderSelectListEntity())
