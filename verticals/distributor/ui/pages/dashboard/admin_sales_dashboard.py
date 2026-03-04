# verticals/distributor/ui/pages/dashboard/admin_sales_dashboard.py

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
        key="distributor.admin_sales.dashboard",
        entity="dashboard",
        domain="distributor",
        path="/dashboard/admin-sales",
        title="Admin Sales Dashboard",
        permissions=[DistributorPermission.ADMIN_SALES_DASHBOARD_VIEW], 
        description="Sales Order & Invoice Processing",
        data_source="/entities/distributor/admin_sales.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Sales Processing",
                items=[
                    ShortcutItem(key="so_entry", label="Sales Order Entry", icon="edit", to="/sales/orders/create"),
                    ShortcutItem(key="invoice_gen", label="Invoice Generation", icon="file-text", to="/sales/invoice/generate"),
                    ShortcutItem(key="so_monitor", label="SO Monitoring", icon="eye", to="/sales/orders"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="so_today", title="SO Today", data_key="so_today"),
                    StatBlock(key="invoice_today", title="Invoice Today", data_key="invoice_today"),
                ]
            ),

            ListViewBlock(
                title="Pending Orders",
                data_key="pending_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="order_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="order_date"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[DistributorPermission.ADMIN_SALES_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("distributor", UI_PAGES)