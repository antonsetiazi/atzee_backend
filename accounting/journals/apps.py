from django.apps import AppConfig


class JournalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounting.journals"
    label = "accounting_journals"


    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from accounting.journals.entities.journal_list import JournalListEntity

        register_entity(JournalListEntity())
