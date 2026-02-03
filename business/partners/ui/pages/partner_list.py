# business/partners/ui/pages/partner_list.py
from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="partners.list",
    entity="partners",
    domain="business",
    title="Partners",
    permissions=["business.partners.view"],
    blocks=[
        TableBlock(
            data_source="/entities/business/partners.list/query/",
            search_mode="client",
            columns=[
                TableColumn(key="code", label="Code"),
                TableColumn(key="name", label="Name"),
                TableColumn(key="email", label="Email"),
                TableColumn(key="phone", label="Phone"),
                TableColumn(key="is_active", label="Active"),
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="edit",
                    to="/business/partners/{id}/edit",
                    permission="business.partners.update"
                ),
                Action(
                    type="delete",
                    label="Delete",
                    icon="delete",
                    permission="business.partners.delete",
                    confirm={
                        "title": "Delete Partner",
                        "message": "Are you sure you want to delete this partner?",
                        "level": "danger",
                    },
                    endpoint="/business/partners/{id}/"
                ),
            ],
            top_actions=[
                Action(
                    type="navigate",
                    label="Create Partner",
                    to="/business/partners/create",
                    permission="business.partners.add"
                )
            ]
        )
    ]
)
