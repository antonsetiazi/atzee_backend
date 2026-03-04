# verticals/distributor/ui/pages/dashboard/finance_manager_dashboard.py

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
        key="distributor.finance_manager.dashboard",
        entity="dashboard",
        domain="distributor",
        path="/dashboard/finance-manager",
        title="Finance Manager Dashboard",
        permissions=[DistributorPermission.FINANCE_MANAGER_DASHBOARD_VIEW],
        description="Receivable & Payment Overview", 
        data_source="/entities/distributor/finance_manager.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Finance Monitoring",
                items=[
                    ShortcutItem(key="invoice_list", label="Invoice List", icon="file-text", to="/finance/invoices"),
                    ShortcutItem(key="payment", label="Incoming Payment", icon="credit-card", to="/finance/payment"),
                    ShortcutItem(key="aging", label="Aging Report", icon="clock", to="/finance/aging"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_receivable", title="Total Receivable", data_key="total_receivable"),
                    StatBlock(key="overdue_amount", title="Overdue Amount", data_key="overdue_amount"),
                    StatBlock(key="daily_collection", title="Daily Collection", data_key="daily_collection"),
                ]
            ),

            ListViewBlock(
                title="Customer Ledger Snapshot",
                data_key="customer_ledger_summary",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="customer_name"),
                    subtitle=ListFieldSchema(key="balance"),
                    description=ListFieldSchema(key="credit_limit"),
                ),
                permissions=[DistributorPermission.FINANCE_MANAGER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("distributor", UI_PAGES)