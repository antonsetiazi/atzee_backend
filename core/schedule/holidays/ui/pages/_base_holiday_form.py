# core/schedule/holidays/ui/pages/_base_holiday_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_holiday_form_page(
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
        Field(key="name", label="Holiday Name", type="text", required=True),
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
            key="all_day",
            label="All Day",
            type="boolean",
            default=True,
        ),
        Field(
            key="recurring",
            label="Recurring",
            type="boolean",
            default=False,
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
        entity="holidays",
        domain=domain,
        path=path,
        title="Holiday",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Define holiday / blackout period",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=redirect_page),
                ],
                refresh_cache=["holidays.list"],
            )
        ],
    )
