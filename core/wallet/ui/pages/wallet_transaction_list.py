# core/wallet/ui/pages/wallet_transaction_list.py

from core.ui.registry import register_ui_module_pages
from core.wallet.ui.pages._base_wallet_transaction_list import (
    build_wallet_transaction_list_page,
)

from core.enum.permissions import CorePermission

UI_PAGES = build_wallet_transaction_list_page(
    key="wallet_transactions.list",
    domain="core",
    title_page="Wallet Transactions",
    subtitle_page="Monitor all wallet ledger activities",
    path="/admin/wallet-transactions",
    data_source="/entities/core/wallet_transactions.list/query/",
    permissions=[CorePermission.ADMIN_WALLET_TRANSACTIONS_VIEW],
    detail_path="/admin/wallet-transactions/{id}",
    search_mode="server",
)

register_ui_module_pages("core", UI_PAGES)