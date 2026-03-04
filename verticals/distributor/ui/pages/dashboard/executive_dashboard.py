# verticals/distributor/ui/pages/dashboard/executive_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.distributor.enum.permissions import DistributorPermission


UI_PAGES = [
    Page(
        key="distributor.executive.dashboard",
        entity="dashboard",
        domain="distributor",
        path="/dashboard",
        title="Executive Dashboard",
        permissions=[DistributorPermission.EXECUTIVE_DASHBOARD_VIEW], 
        description="Business Performance Overview",
        data_source="/entities/distributor/executive.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Executive Reports",
                items=[
                    ShortcutItem(key="sales_report", label="Sales Report", icon="bar-chart", to="/reports/sales"),
                    ShortcutItem(key="margin_report", label="Margin Report", icon="percent", to="/reports/margin"),
                    ShortcutItem(key="aging_report", label="Aging Report", icon="clock", to="/reports/aging"),
                    ShortcutItem(key="inventory_valuation", label="Inventory Valuation", icon="archive", to="/reports/inventory"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="sales_today", title="Sales Today", data_key="sales_today"),
                    StatBlock(key="gross_profit", title="Gross Profit", data_key="gross_profit"),
                    StatBlock(key="outstanding_ar", title="Outstanding Receivable", data_key="outstanding_ar"),
                    StatBlock(key="return_rate", title="Return Rate", data_key="return_rate", suffix="%"),
                ]
            ),

            ListViewBlock(
                title="Top Salesman This Month",
                data_key="top_salesman",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="salesman_name"),
                    subtitle=ListFieldSchema(key="territory"),
                    description=ListFieldSchema(key="total_sales"),
                ),
                permissions=[DistributorPermission.EXECUTIVE_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("distributor", UI_PAGES)