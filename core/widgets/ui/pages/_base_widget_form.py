# core/widgets/ui/pages/_base_widget_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action
from core.widgets.types.xregistry import WIDGET_TYPE_FIELDS


def build_widget_form_page(
    *,
    request=None,
    key: str,
    domain: str,
    path: str,
    title_page: str,
    submit_to: str,
    method: str,
    permissions: list[str],
    title: str,
    widget_type: str,
    redirect_page: str,
    extra_fields: list[Field] | None = None,
):

    fields = [
        Field(key="type", type="hidden", label="Widget Type", required=True, default=widget_type),
        Field(
            key="position",
            label="Position",
            type="select",
            required=True,
            options=[
                {"value": "dashboard.main", "label": "Dashboard Main"},
                {"value": "dashboard.sidebar", "label": "Dashboard Sidebar"},
                {"value": "app.main", "label": "App Main"},
                {"value": "app.sidebar", "label": "App Sidebar"},
            ],
        ),
        Field(
            key="title",
            label="Title",
            type="text",
            required=False,
        ),
        Field(
            key="starts_at",
            label="Starts At",
            type="datetime",
            required=False,
        ),
        Field(
            key="ends_at",
            label="Ends At",
            type="datetime",
            required=False,
        ),
        Field(
            key="target_roles",
            label="Target Roles",
            type="json",
            required=False,
            default=[]
        ),
        Field(
            key="target_permissions",
            label="Target Permissions",
            type="json",
            required=False,
            default=[]
        ),
        Field(
            key="target_apps",
            label="Target Apps",
            type="json",
            required=False,
            default=[]
        ),
        Field(
            key="order",
            label="Order",
            type="number",
            required=False,
            default=50,
        ),
        Field(
            key="is_active",
            label="Active",
            type="boolean",
            required=False,
            default=True,
        ),
    ]

    if extra_fields:
        fields = fields + extra_fields

    # config_fields = []

    # widget_type = None
    # if request:
    #     widget_type = request.GET.get("type")

    # if widget_type and widget_type in WIDGET_TYPE_FIELDS:
    #     config_fields = WIDGET_TYPE_FIELDS[widget_type]()

    # fields = fields + config_fields

    return Page(
        key=key,
        entity="widgets",
        domain=domain,
        path=path,
        title=title_page,
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(
                        type="redirect",
                        label="Cancel",
                        to=redirect_page,
                    ),
                ],
            )
        ],
    )
