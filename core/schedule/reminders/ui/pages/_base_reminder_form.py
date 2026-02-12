# core/schedule/reminders/ui/pages/_base_reminder_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_reminder_form_page(
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
        Field(
            key="event",
            label="Event",
            type="select",
            required=True,
            data_source="/entities/core/schedule.events.select.list/query/",
        ),
        Field(
            key="reminder_time",
            label="Reminder Time (Before Event)",
            type="duration",
            required=True,
        ),
        Field(
            key="reminder_type",
            label="Reminder Type",
            type="select",
            required=True,
            options=[
                {"value": "email", "label": "Email"},
                {"value": "in_app", "label": "In-App"},
                {"value": "wa", "label": "WhatsApp"},
            ],
        ),
        Field(
            key="repeat_interval",
            label="Repeat Interval",
            type="duration",
        ),
    ]

    if extra_fields:
        fields += extra_fields

    return Page(
        key=key,
        entity="reminders",
        domain=domain,
        path=path,
        title="Reminder",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data reminder dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=redirect_page),
                ],
            ),
        ],
    )
