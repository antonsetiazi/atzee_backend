# core/files/ui/pages/_base_file_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_file_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    upload_path: str,
    delete_endpoint: str,
):
    columns = [
        TableColumn(key="filename", label="File Name"),
        TableColumn(key="file_type", label="Type"),
        TableColumn(key="size", label="Size"),
        TableColumn(key="uploaded_by", label="Uploaded By"),
        TableColumn(key="created_at", label="Uploaded At"),
    ]

    return Page(
        key=key,
        entity="files",
        domain=domain,
        path=path,
        title="Files",
        permissions=permissions,
        blocks=[
            TableBlock(
                data_source=data_source,
                search_mode="server",
                columns=columns,
                actions=[
                    Action(
                        type="link",
                        label="Download",
                        icon="download",
                        to="{url}",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.files.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete File",
                            "message": "Are you sure you want to delete this file?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Upload File",
                        icon="upload",
                        to=upload_path,
                        permission="core.files.add",
                    )
                ],
            )
        ],
    )
