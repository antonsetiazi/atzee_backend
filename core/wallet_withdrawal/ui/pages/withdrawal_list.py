# core/wallet_withdrawal/ui/pages/withdrawal_list.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn, ActionBlock
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission


UI_PAGES = Page(
    key="withdrawals.list",
    entity="withdrawals",
    domain="core",

    path="/admin/withdrawals",

    title="Withdrawals",
    subtitle="Monitor and manage all withdrawal requests",

    permissions=[
        CorePermission.ADMIN_WALLET_WITHDRAWAL_VIEW
    ],

    data_source="/entities/core/withdrawals.list/query/",

    blocks=[
        TableBlock(
            title="Daftar Bank",
            data_key="items",
            search_mode="server",

            columns=[

                # 👤 USER (penting banget)
                TableColumn(key="user_name", label="User"),

                # 🔄 status
                TableColumn(
                    key="status",
                    label="Status",
                    align="center",
                ),

                TableColumn(key="id", label="ID"),
                
                TableColumn(key="user_phone", label="Phone"),

                # 💰 amount
                TableColumn(
                    key="amount",
                    label="Amount",
                    format="currency",
                    align="right",
                ),
                TableColumn(
                    key="fee",
                    label="Fee",
                    format="currency",
                    align="right",
                ),
                TableColumn(
                    key="net_amount",
                    label="Net",
                    format="currency",
                    align="right",
                ),

                # 🏦 destination
                TableColumn(key="destination_label", label="Destination"),                

                # ⏱️ processed time
                TableColumn(
                    key="processed_at",
                    label="Processed At",
                    format="datetime",
                ),
            ],

            actions=[
                Action(
                    type="navigate",
                    label="Action",
                    icon="pencil",
                    to="/admin/withdrawals/approve/{id}",
                    permission=CorePermission.ADMIN_WALLET_WITHDRAWAL_VIEW,
                )
            ],
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)