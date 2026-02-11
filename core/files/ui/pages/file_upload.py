# core/files/ui/pages/file_upload.py

from core.files.ui.pages._base_file_form import build_file_upload_page

UI_PAGES = build_file_upload_page(
    key="files.upload",
    domain="core",
    path="/core/files/upload",
    submit_to="/files/",
    permissions=["core.files.add"],
    redirect_page="/core/files",
)
