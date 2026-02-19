# core/files/apps.py

from django.apps import AppConfig


class FilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.files"
    label = "core_files"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from core.files.entities.file_list import FileListEntity
        from core.files.entities.file_select_list import FileSelectListEntity
        from core.files.entities.file_my_list import FileMyListEntity

        register_entity(FileListEntity())
        register_entity(FileSelectListEntity())
        register_entity(FileMyListEntity())
