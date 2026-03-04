# verticals/isp/ui/pages/dashboard/cs_dashboard.py

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
        key="isp.cs.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard",
        title="Customer Service Dashboard",
        permissions=[IspPermission.CS_DASHBOARD_VIEW], 
        description="Customer & Ticket Operations",
        data_source="/entities/isp/cs.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Customer Operations",
                items=[
                    ShortcutItem(key="customers", label="Customers", icon="users", to="/customers"),
                    ShortcutItem(key="subscriptions", label="Subscriptions", icon="wifi", to="/subscriptions"),
                    ShortcutItem(key="tickets", label="Trouble Tickets", icon="life-buoy", to="/operations/tickets"),
                    ShortcutItem(key="work_orders", label="Work Orders", icon="tool", to="/operations/work-orders"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="active_customers", title="Active Customers", data_key="active_customers"),
                    StatBlock(key="open_tickets", title="Open Tickets", data_key="open_tickets"),
                    StatBlock(key="installations_today", title="Installations Today", data_key="installations_today"),
                ],
            ),

            ListViewBlock(
                title="Recent Customer Tickets",
                data_key="recent_tickets",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="ticket_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="issue_summary"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[IspPermission.CS_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)