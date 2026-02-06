# src/accounting/chart_of_accounts/ui/pages/chart_of_account_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="chart_of_accounts.list",
    domain="accounting",
    entity="chart_of_accounts",
    path="/accounting/chart-of-accounts",
    title="Chart of Accounts",
    permissions=["accounting.chart_of_accounts.view"],
    blocks=[
        TableBlock(
            data_source="/entities/accounting/chart_of_accounts.list/query/",
            search_mode="client",
            columns=[
                TableColumn(key="code", label="Code"),
                TableColumn(key="name", label="Account Name"),
                TableColumn(key="account_type", label="Type"),
                TableColumn(key="parent_name", label="Parent"),
                TableColumn(key="is_active_label", label="Active"),
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    to="/accounting/chart-of-accounts/{id}/edit",
                    permission="accounting.chart_of_accounts.update",
                ),
                Action(
                    type="delete",
                    label="Delete",
                    permission="accounting.chart_of_accounts.delete",
                    confirm={
                        "title": "Delete Account",
                        "message": "Deleting an account may affect financial reports. Are you sure?",
                        "level": "danger",
                    },
                    endpoint="/accounting/chart-of-accounts/{id}/",
                ),
            ],
            top_actions=[
                Action(
                    type="navigate",
                    label="Create Account",
                    to="/accounting/chart-of-accounts/create",
                    permission="accounting.chart_of_accounts.add",
                )
            ],
        )
    ],
)
