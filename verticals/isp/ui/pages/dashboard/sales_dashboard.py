# verticals/isp/ui/pages/dashboard/sales_dashboard.py

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

from verticals.isp.enum.permissions import IspPermission


UI_PAGES = [
    Page(
        key="isp.sales.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard",
        title="Sales & Marketing Dashboard",
        permissions=[IspPermission.SALES_DASHBOARD_VIEW], 
        description="Leads & Sales Performance Overview",
        data_source="/entities/isp/sales.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Sales Tools",
                items=[
                    ShortcutItem(key="leads", label="Leads", icon="target", to="/sales/leads"),
                    ShortcutItem(key="sales_orders", label="Sales Orders", icon="shopping-cart", to="/sales/orders"),
                    ShortcutItem(key="promotions", label="Promotions", icon="gift", to="/sales/promotions"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="new_leads", title="New Leads", data_key="new_leads"),
                    StatBlock(key="conversion_rate", title="Conversion Rate", data_key="conversion_rate", suffix="%"),
                    StatBlock(key="monthly_sales", title="Monthly Sales", data_key="monthly_sales"),
                ],
            ),

            ListViewBlock(
                title="Recent Leads",
                data_key="recent_leads",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="lead_name"),
                    subtitle=ListFieldSchema(key="contact_number"),
                    description=ListFieldSchema(key="area"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[IspPermission.SALES_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)