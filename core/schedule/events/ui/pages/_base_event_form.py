# core/schedule/events/ui/pages/_base_event_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, FileBlock, TagBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_event_form_page(
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
        Field(key="title", label="Event Title", type="text", required=True),
        Field(key="description", label="Description", type="textarea"),
        Field(key="start_datetime", label="Start Datetime", type="datetime", required=True),
        Field(key="end_datetime", label="End Datetime", type="datetime", required=True),
        Field(key="all_day", label="All Day", type="boolean"),
        Field(key="participants", label="Participants (User IDs)", type="json", required=False, default=[],),
        Field(key="color", label="Color", type="text"),
        Field(key="metadata", label="Metadata", type="json", required=False, default={},),
    ]

    if extra_fields:
        fields += extra_fields

    return Page(
        key=key,
        entity="events",
        domain=domain,
        path=path,
        title="Event",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data event dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=redirect_page),
                ],
            ),

            # 🔽 FILE ATTACHMENTS (opsional, jika event perlu attachment)
            FileBlock(
                title="Event Files",
                entity_type="event",
                entity_id_from="id",
                multiple=True,
                accept="image/*,.pdf",
                permissions=["core.schedule.events.update"],
            ),

            # 🔽 TAGS
            TagBlock(
                title="Event Tags",
                entity_type="core_schedule_events.event",
                entity_id_from="id",
                allow_create=True,
                allow_attach=True,
                allow_detach=True,
                multiple=True,
                permissions=["core.schedule.events.update"],
            ),
        ],
    )
