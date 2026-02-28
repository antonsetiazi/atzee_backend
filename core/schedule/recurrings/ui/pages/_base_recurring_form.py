# core/schedule/recurrings/ui/pages/_base_recurring_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_recurring_form_page(
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
            key="frequency",
            label="Frequency",
            type="select",
            required=True,
            options=[
                {"value": "daily", "label": "Daily"},
                {"value": "weekly", "label": "Weekly"},
                {"value": "monthly", "label": "Monthly"},
                {"value": "yearly", "label": "Yearly"},
            ],
        ),
        Field(
            key="interval",
            label="Interval",
            type="number",
            required=True,
        ),
        Field(
            key="end_date",
            label="End Date",
            type="date",
        ),
    ]

    if extra_fields:
        fields += extra_fields

    return Page(
        key=key,
        entity="recurrings",
        domain=domain,
        path=path,
        title="Recurring",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Configure recurring rule for the selected event",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=redirect_page),
                ],
                refresh_cache=["recurrings.list"],
            ),
        ],
    )
