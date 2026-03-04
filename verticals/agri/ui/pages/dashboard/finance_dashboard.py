# verticals/agri/ui/pages/dashboard/finance_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.agri.enum.permissions import AgriPermission


UI_PAGES = [
    Page(
        key="agri.finance.dashboard",
        entity="dashboard", 
        domain="agri",
        path="/dashboard",
        title="Finance Dashboard",
        permissions=[AgriPermission.FINANCE_DASHBOARD_VIEW],
        description="Agriculture Financial Overview",
        data_source="/entities/agri/finance.dashboard/query/",
        blocks=[

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_expense", title="Total Expense", data_key="total_expense"),
                    StatBlock(key="total_revenue", title="Total Revenue", data_key="total_revenue"),
                    StatBlock(key="profit", title="Net Profit", data_key="profit"),
                    StatBlock(key="cost_per_hectare", title="Cost / Hectare", data_key="cost_per_hectare"),
                ]
            ),

            ListViewBlock(
                title="Recent Farm Expenses",
                data_key="recent_expenses",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="expense_type"),
                    subtitle=ListFieldSchema(key="plot_name"),
                    description=ListFieldSchema(key="date"),
                    trailing=ListFieldSchema(key="amount"),
                ),
                permissions=[AgriPermission.FINANCE_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("agri", UI_PAGES)