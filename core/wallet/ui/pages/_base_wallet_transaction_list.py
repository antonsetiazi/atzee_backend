# core/wallet/ui/pages/_base_wallet_transaction_list.py

from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page


def build_wallet_transaction_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    title_page: str,
    subtitle_page: str,
    data_source: str,
    permissions: list[str],
    detail_path: str,
    search_mode: str,
):
    columns = [
        # 🔗 identity
        TableColumn(key="id", label="ID"),
        # 👤 user
        TableColumn(key="user_name", label="User"),
        TableColumn(key="user_phone", label="Phone"),
        # 💳 wallet
        TableColumn(key="wallet_id", label="Wallet"),
        # 💰 amount
        TableColumn(
            key="amount",
            label="Amount",
            format="currency",
            align="right",
            weight="semibold",
        ),
        # 🔄 type
        TableColumn(
            key="transaction_type",
            label="Type",
            align="center",
            size="xs",
        ),
        # 🔗 reference
        TableColumn(key="reference_type", label="Ref Type"),
        TableColumn(key="reference_id", label="Reference"),
        # 📝 description
        TableColumn(key="description", label="Description", size="xs"),
        # 🔐 idempotency
        TableColumn(key="idempotency_key", label="Idempotency"),
        # ⏱️ created
        TableColumn(
            key="created_at",
            label="Created",
            format="datetime",
            size="xs",
            text_style="muted",
        ),
    ]

    return Page(
        key=key,
        entity="wallet_transactions",
        domain=domain,
        path=path,
        title=title_page,
        subtitle=subtitle_page,
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                title="Wallet Transactions",
                data_key="items",
                search_mode=search_mode,
                columns=columns,
                detail_as_state=False,
                actions=[
                    Action(
                        type="navigate",
                        label="View",
                        icon="eye",
                        to=detail_path,
                        permission="core.wallet.transactions.view",
                    ),
                ],
                top_actions=[],
            )
        ],
    )
