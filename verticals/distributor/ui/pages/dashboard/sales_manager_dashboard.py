# verticals/distributor/ui/pages/dashboard/sales_manager_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock, StatBlock,
    ShortcutBlock, ShortcutItem,
    ListViewBlock, ListFieldSchema, ListTileSchema,
)

from verticals.distributor.enum.permissions import DistributorPermission


UI_PAGES = [
    Page(
        key="distributor.sales_manager.dashboard",
        entity="dashboard",
        domain="distributor",
        path="/dashboard",
        title="Sales Manager Dashboard",
        permissions=[DistributorPermission.SALES_MANAGER_DASHBOARD_VIEW], 
        description="Sales Performance & Territory Monitoring",
        data_source="/entities/distributor/sales_manager.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Sales Monitoring",
                items=[
                    ShortcutItem(key="sales_order", label="Sales Order", icon="shopping-cart", to="/sales/orders"),
                    ShortcutItem(key="invoice", label="Invoice Monitoring", icon="file-text", to="/sales/invoices"),
                    ShortcutItem(key="credit_limit", label="Credit Limit", icon="shield", to="/monitoring/credit-limit"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="target_vs_real", title="Target vs Realisasi", data_key="target_vs_real"),
                    StatBlock(key="outstanding_order", title="Outstanding Order", data_key="outstanding_order"),
                    StatBlock(key="sales_growth", title="Sales Growth", data_key="sales_growth", suffix="%"),
                ]
            ),

            ListViewBlock(
                title="Salesman Ranking",
                data_key="salesman_ranking",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="salesman_name"),
                    subtitle=ListFieldSchema(key="territory"),
                    description=ListFieldSchema(key="achievement"),
                ),
                permissions=[DistributorPermission.SALES_MANAGER_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("distributor", UI_PAGES)