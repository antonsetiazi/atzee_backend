# verticals/pesantren/ui/pages/dashboard/bendahara_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
)

from verticals.pesantren.enum.permissions import PesantrenPermission


UI_PAGES = [
    Page(
        key="pesantren.bendahara.dashboard",
        entity="dashboard",
        domain="pesantren",
        path="/dashboard",
        title="Dashboard Keuangan",
        permissions=[PesantrenPermission.BENDAHARA_DASHBOARD_VIEW], 
        description="Monitoring Keuangan",
        data_source="/entities/pesantren/bendahara.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Keuangan",
                items=[
                    ShortcutItem(key="tagihan", label="Tagihan SPP", icon="file-text", to="/keuangan/tagihan"),
                    ShortcutItem(key="pembayaran", label="Pembayaran", icon="credit-card", to="/keuangan/pembayaran"),
                    ShortcutItem(key="jurnal", label="Jurnal", icon="book", to="/accounting/jurnal"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="income", title="Total Income", data_key="income"),
                    StatBlock(key="expense", title="Total Expense", data_key="expense"),
                    StatBlock(key="cash_balance", title="Cash Balance", data_key="cash_balance"),
                ],
            ),
        ],
    ),
]

register_ui_module_pages("pesantren", UI_PAGES)