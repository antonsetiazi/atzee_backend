# verticals/isp/ui/pages/dashboard/billing_dashboard.py

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
        key="isp.billing.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard",
        title="Billing Dashboard",
        permissions=[IspPermission.BILLING_DASHBOARD_VIEW], 
        description="Invoice & Payment Management",
        data_source="/entities/isp/billing.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Billing Tools",
                items=[
                    ShortcutItem(key="invoices", label="Invoices", icon="file-text", to="/billing/invoices"),
                    ShortcutItem(key="payments", label="Payments", icon="credit-card", to="/billing/payments"),
                    ShortcutItem(key="recurring", label="Recurring Billing", icon="repeat", to="/billing/recurring"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="outstanding_ar", title="Outstanding AR", data_key="outstanding_ar"),
                    StatBlock(key="overdue_count", title="Overdue Invoices", data_key="overdue_count"),
                    StatBlock(key="collected_today", title="Collected Today", data_key="collected_today"),
                ],
            ),

            ListViewBlock(
                title="Overdue Customers",
                data_key="overdue_customers",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="customer_name"),
                    subtitle=ListFieldSchema(key="invoice_number"),
                    description=ListFieldSchema(key="due_date"),
                    status=ListFieldSchema(key="aging_status"),
                ),
                permissions=[IspPermission.BILLING_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)