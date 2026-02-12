# core/schedule/shifts/ui/pages/_base_shift_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, TagBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_shift_form_page(
    *,
    key: str,
    domain: str,
    path: str,
    submit_to: str,
    method: str,
    permissions: list[str],
    title: str,
    redirect_page: str,
    extra_fields: list[Field] | None = None,
):
    fields = [
        Field(key="name", label="Shift Name", type="text", required=True),
        Field(
            key="start_datetime",
            label="Start Datetime",
            type="datetime",
            required=True,
        ),
        Field(
            key="end_datetime",
            label="End Datetime",
            type="datetime",
            required=True,
        ),
        Field(
            key="participants",
            label="Participants",
            type="json",
            default=[],
            required=False,
        ),
        Field(
            key="metadata",
            label="Metadata",
            type="json",
            required=False,
            default={},
        ),
    ]

    if extra_fields:
        fields += extra_fields

    return Page(
        key=key,
        entity="shifts",
        domain=domain,
        path=path,
        title="Shift",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data shift dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=redirect_page),
                ],
            ),

            # TAGS (optional engine support)
            TagBlock(
                title="Shift Tags",
                entity_type="core_schedule_shifts.shift",
                entity_id_from="id",
                allow_create=True,
                allow_attach=True,
                allow_detach=True,
                multiple=True,
                permissions=["core.schedule.shifts.update"],
            ),
        ],
    )
