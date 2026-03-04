# verticals/koperasi/ui/pages/dashboard/bendahara_dashboard.py

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

from verticals.koperasi.enum.permissions import KoperasiPermission


UI_PAGES = [
    Page(
        key="koperasi.bendahara.dashboard",
        entity="dashboard",
        domain="koperasi",
        path="/dashboard",
        title="Bendahara Dashboard",
        permissions=[KoperasiPermission.BENDAHARA_DASHBOARD_VIEW], 
        description="Financial Operations Overview",
        data_source="/entities/koperasi/bendahara.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Finance Action",
                items=[
                    ShortcutItem(key="input_savings", label="Input Simpanan", icon="plus-circle", to="/savings/input"),
                    ShortcutItem(key="withdrawal", label="Penarikan", icon="minus-circle", to="/savings/withdraw"),
                    ShortcutItem(key="disburse_loan", label="Cairkan Pinjaman", icon="send", to="/loans/disburse"),
                    ShortcutItem(key="receive_installment", label="Terima Angsuran", icon="repeat", to="/loans/installment"),
                ],
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="cash_balance", title="Cash Balance", data_key="cash_balance"),
                    StatBlock(key="today_transactions", title="Transactions Today", data_key="today_transactions"),
                    StatBlock(key="loan_outstanding", title="Loan Outstanding", data_key="loan_outstanding"),
                ]
            ),

            ListViewBlock(
                title="Recent Transactions",
                data_key="recent_transactions",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="member_name"),
                    subtitle=ListFieldSchema(key="amount"),
                    description=ListFieldSchema(key="transaction_type"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[KoperasiPermission.BENDAHARA_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("koperasi", UI_PAGES)