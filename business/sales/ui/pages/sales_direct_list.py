# business/sales/ui/pages/sales_direct_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="sales.direct.list",
    entity="sales.direct",
    domain="business",
    path="/business/sales/direct",
    title="Direct Sales",
    permissions=["business.sales.view"],
    blocks=[
        TableBlock(
            data_source="/entities/business/sales.direct.list/query/",
            search_mode="client",
            columns=[
                TableColumn(key="reference", label="Reference"),
                TableColumn(key="transaction_date", label="Date"),
                TableColumn(key="notes", label="Notes"),
                TableColumn(key="status", label="Status"),
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Detail",
                    icon="view",
                    to="/business/sales.direct/{id}",
                    permission="business.sales.view",
                ),
                Action(
                    type="navigate",
                    label="Edit",
                    icon="edit",
                    to="/business/sales.direct/{id}/edit",
                    permission="business.sales.update",
                    when={"status": "draft"},
                ),
                Action(
                    type="delete",
                    label="Delete",
                    icon="delete",
                    permission="business.sales.delete",
                    confirm={
                        "title": "Delete Sales",
                        "message": "Are you sure you want to delete this sales transaction?",
                        "level": "danger",
                    },
                    endpoint="/business/sales/direct/{id}/",
                ),
            ],
            top_actions=[
                Action(
                    type="navigate",
                    label="Create Direct Sales",
                    icon="create",
                    to="/business/sales.direct/create",
                    permission="business.sales.add",
                )
            ],
        )
    ],
)
