# verticals/isp/ui/pages/dashboard/customer_portal_dashboard.py

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
        key="isp.customer.portal.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard",
        title="My Dashboard",
        permissions=[IspPermission.CUSTOMER_PORTAL_VIEW], 
        description="Customer Self-Service Portal",
        data_source="/entities/isp/customer.portal.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="My Account",
                items=[
                    ShortcutItem(key="subscription", label="My Subscription", icon="wifi", to="/portal/subscription"),
                    ShortcutItem(key="invoices", label="My Invoices", icon="file-text", to="/portal/invoices"),
                    ShortcutItem(key="support", label="Support Tickets", icon="life-buoy", to="/portal/tickets"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="connection_status", title="Connection Status", data_key="connection_status"),
                    StatBlock(key="current_usage", title="Usage This Month", data_key="usage_summary"),
                ],
            ),

            ListViewBlock(
                title="Recent Invoices",
                data_key="recent_invoices",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="invoice_number"),
                    subtitle=ListFieldSchema(key="amount"),
                    description=ListFieldSchema(key="due_date"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[IspPermission.CUSTOMER_PORTAL_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)