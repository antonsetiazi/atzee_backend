# verticals/isp/ui/pages/dashboard/gm_dashboard.py

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
        key="isp.gm.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard",
        title="General Manager Dashboard", 
        permissions=[IspPermission.GM_DASHBOARD_VIEW],
        description="Business KPI & Operational Overview",
        data_source="/entities/isp/gm.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Management Access",
                items=[
                    ShortcutItem(key="customers", label="Customers", icon="users", to="/customers"),
                    ShortcutItem(key="subscriptions", label="Subscriptions", icon="wifi", to="/subscriptions"),
                    ShortcutItem(key="tickets", label="Tickets", icon="life-buoy", to="/operations/tickets"),
                    ShortcutItem(key="financial", label="Financial Reports", icon="bar-chart", to="/finance/reports"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="monthly_revenue", title="Monthly Revenue", data_key="monthly_revenue"),
                    StatBlock(key="active_customers", title="Active Customers", data_key="active_customers"),
                    StatBlock(key="open_tickets", title="Open Tickets", data_key="open_tickets"),
                    StatBlock(key="network_health", title="Network Health", data_key="network_health", suffix="%"),
                ],
            ),

            ListViewBlock(
                title="SLA Critical Tickets",
                data_key="critical_tickets",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="ticket_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="issue_type"),
                    status=ListFieldSchema(key="priority"),
                ),
                permissions=[IspPermission.GM_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)