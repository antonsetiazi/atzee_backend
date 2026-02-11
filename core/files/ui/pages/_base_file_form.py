# core/files/ui/pages/_base_file_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_file_upload_page(
    *,
    key: str,
    domain: str,
    path: str,
    submit_to: str,
    permissions: list[str],
    redirect_page: str,
):
    fields = [
        Field(
            key="file",
            label="File",
            type="file",
            required=True,
        ),
        Field(
            key="description",
            label="Description",
            type="textarea",
            required=False,
            default="",
        ),
    ]

    return Page(
        key=key,
        entity="files",
        domain=domain,
        path=path,
        title="Upload File",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method="POST",
                title="Upload File",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Upload"),
                    Action(
                        type="redirect",
                        label="Cancel",
                        to=redirect_page,
                    ),
                ],
            )
        ],
    )
