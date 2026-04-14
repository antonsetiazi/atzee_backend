# core/wallet_withdrawal/ui/pages/_base_withdrawal_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_withdrawal_list_page(
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

        # 👤 USER (penting banget)
        TableColumn(key="user_name", label="User"),
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

        # 🔄 status
        TableColumn(
            key="status",
            label="Status",
            align="center",
        ),

        # ⏱️ processed time
        TableColumn(
            key="processed_at",
            label="Processed At",
            format="datetime",
        ),
    ]

    return Page(
        key=key,
        entity="withdrawals",
        domain=domain,
        path=path,
        title=title_page,
        subtitle=subtitle_page,
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                title="Withdrawal Requests",
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
                        permission="core.wallet_withdrawal.view",
                    ),
                ],
                top_actions=[],
            )
        ],
    )