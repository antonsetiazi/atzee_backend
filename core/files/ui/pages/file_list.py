# core/files/ui/pages/file_list.py

from core.ui.registry import register_ui_module_pages
from core.files.ui.pages._base_file_list import build_file_list_page

UI_PAGES = build_file_list_page(
    key="files.list",
    domain="core",
    path="/core/files",
    data_source="/entities/core/files.list/query/",
    permissions=["core.files.view"],
    upload_path="/core/files/upload",
    delete_endpoint="/files/{id}/",
)

register_ui_module_pages("core", UI_PAGES)