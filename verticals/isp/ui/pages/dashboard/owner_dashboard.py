# verticals/isp/ui/pages/dashboard/owner_dashboard.py

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
        key="isp.owner.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard/owner",
        title="Owner Dashboard",
        permissions=[IspPermission.OWNER_DASHBOARD_VIEW], 
        description="Full ISP Business Overview",
        data_source="/entities/isp/owner.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Control",
                items=[
                    ShortcutItem(key="financial_reports", label="Financial Reports", icon="bar-chart", to="/finance/reports"),
                    ShortcutItem(key="devices", label="Device Configuration", icon="server", to="/network/devices"),
                    ShortcutItem(key="integrations", label="Integrations", icon="link", to="/settings/integrations"),
                    ShortcutItem(key="tenant", label="Tenant Settings", icon="settings", to="/settings/tenant"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_revenue", title="Total Revenue", data_key="total_revenue"),
                    StatBlock(key="active_customers", title="Active Customers", data_key="active_customers"),
                    StatBlock(key="network_uptime", title="Network Uptime", data_key="network_uptime", suffix="%"),
                    StatBlock(key="net_profit", title="Net Profit", data_key="net_profit"),
                ],
            ),

            ListViewBlock(
                title="Recent High Value Transactions",
                data_key="recent_financial_activity",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="invoice_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="amount"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[IspPermission.OWNER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)