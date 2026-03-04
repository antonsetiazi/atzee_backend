# verticals/isp/ui/pages/dashboard/finance_dashboard.py

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
        key="isp.finance.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard/finance",
        title="Finance Manager Dashboard",
        permissions=[IspPermission.FINANCE_DASHBOARD_VIEW], 
        description="Financial Performance & Cashflow Overview",
        data_source="/entities/isp/finance.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Finance Tools",
                items=[
                    ShortcutItem(key="invoices", label="Invoices", icon="file-text", to="/billing/invoices"),
                    ShortcutItem(key="payments", label="Payments", icon="credit-card", to="/billing/payments"),
                    ShortcutItem(key="financial_reports", label="Financial Reports", icon="bar-chart", to="/finance/reports"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="monthly_revenue", title="Monthly Revenue", data_key="monthly_revenue"),
                    StatBlock(key="profit", title="Profit", data_key="profit"),
                    StatBlock(key="cashflow", title="Cashflow", data_key="cashflow"),
                    StatBlock(key="ar_aging", title="AR Aging", data_key="ar_aging"),
                ],
            ),

            ListViewBlock(
                title="Recent Large Payments",
                data_key="large_payments",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="customer_name"),
                    subtitle=ListFieldSchema(key="invoice_number"),
                    description=ListFieldSchema(key="amount"),
                    status=ListFieldSchema(key="payment_status"),
                ),
                permissions=[IspPermission.FINANCE_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)