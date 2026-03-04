# verticals/koperasi/ui/pages/dashboard/member_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.koperasi.enum.permissions import KoperasiPermission


UI_PAGES = [
    Page(
        key="koperasi.member.dashboard",
        entity="dashboard",
        domain="koperasi",
        path="/dashboard",
        title="My Dashboard",
        permissions=[KoperasiPermission.MEMBER_DASHBOARD_VIEW], 
        description="Personal Cooperative Overview",
        data_source="/entities/koperasi/member.dashboard/query/",
        blocks=[

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="my_savings_balance", title="My Savings Balance", data_key="savings_balance"),
                    StatBlock(key="my_loan_balance", title="My Loan Balance", data_key="loan_balance"),
                    StatBlock(key="my_shu", title="My SHU", data_key="shu_amount"),
                ]
            ),

            ListViewBlock(
                title="Recent Savings Transactions",
                data_key="my_savings_transactions",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="transaction_date"),
                    subtitle=ListFieldSchema(key="amount"),
                    description=ListFieldSchema(key="type"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[KoperasiPermission.MEMBER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("koperasi", UI_PAGES)