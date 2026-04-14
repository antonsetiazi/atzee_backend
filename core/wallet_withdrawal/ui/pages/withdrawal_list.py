# core/wallet_withdrawal/ui/pages/withdrawal_list.py

from core.ui.registry import register_ui_module_pages
from core.wallet_withdrawal.ui.pages._base_withdrawal_list import (
    build_withdrawal_list_page,
)

from core.enum.permissions import CorePermission

UI_PAGES = build_withdrawal_list_page(
    key="withdrawals.list",
    domain="core",
    title_page="Withdrawals",
    subtitle_page="Monitor and manage all withdrawal requests",
    path="/admin/withdrawals",
    data_source="/entities/core/withdrawals.list/query/",
    permissions=[CorePermission.ADMIN_WALLET_WITHDRAWAL_VIEW],
    detail_path="/admin/withdrawals/{id}",
    search_mode="server",
)

register_ui_module_pages("core", UI_PAGES)