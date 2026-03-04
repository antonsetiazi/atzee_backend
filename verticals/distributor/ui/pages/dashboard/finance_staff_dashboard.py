# # verticals/distributor/ui/pages/dashboard/finance_staff_dashboard.py

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
        key="distributor.finance_staff.dashboard",
        entity="dashboard",
        domain="distributor",
        path="/dashboard/finance-staff",
        title="Finance Staff Dashboard",
        permissions=[DistributorPermission.FINANCE_STAFF_DASHBOARD_VIEW], 
        description="Payment Processing & Ledger Entry",
        data_source="/entities/distributor/finance_staff.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Finance Entry",
                items=[
                    ShortcutItem(key="payment_entry", label="Payment Entry", icon="credit-card", to="/finance/payment"),
                    ShortcutItem(key="invoice_lookup", label="Invoice Lookup", icon="search", to="/finance/invoices"),
                    ShortcutItem(key="ledger", label="Customer Ledger", icon="book", to="/finance/ledger"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="payment_today", title="Payment Today", data_key="payment_today"),
                    StatBlock(key="unallocated_payment", title="Unallocated Payment", data_key="unallocated_payment"),
                ]
            ),

            ListViewBlock(
                title="Recent Payments",
                data_key="recent_payments",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="payment_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="amount"),
                ),
                permissions=[DistributorPermission.FINANCE_STAFF_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("distributor", UI_PAGES)