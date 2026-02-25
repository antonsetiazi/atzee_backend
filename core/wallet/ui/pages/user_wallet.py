# core/wallet/ui/pages/user_wallet.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ListViewBlock,
    ListTileSchema,
    ListFieldSchema,
    TextBlock,
)
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="user.wallet",
    entity="user.wallet",
    domain="core",
    title="My Wallet",
    path="/core/wallet",
    permissions=["core.user.wallet.view"],
    data_source="/entities/core/user.wallet.history/query/",
    description="View wallet balance and transaction history",
    method="POST",
    blocks=[
        # ==============================
        # WALLET SUMMARY
        # ==============================
        ContainerBlock(
            blocks=[
                StatBlock(
                    title="Available Balance",
                    key="balance",
                    meta={
                        "format": "currency",
                        "currency": "IDR"
                    },
                    value=None
                ),
            ],
        ),

        # ==============================
        # TRANSACTION HISTORY
        # ==============================
        ListViewBlock(
            title="Transaction History",
            data_key="items",  # karena endpoint return array langsung
            layout="card",
            tile=ListTileSchema(
                title=ListFieldSchema(
                    key="transaction_type"
                ),
                subtitle=ListFieldSchema(
                    key="reference"
                ),
                description=ListFieldSchema(
                    key="created_at",
                    format="datetime"
                ),
                trailing=ListFieldSchema(
                    key="amount",
                    format="currency",
                    currency="IDR"
                ),
                meta={
                    "Description": ListFieldSchema(
                        key="description"
                    )
                }
            ),
            permissions=["core.user.wallet.view"],
        )
    ]
)

register_ui_module_pages("core", UI_PAGES)