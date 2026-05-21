# business/payment_gateway/ui/pages/_base_payment_gateway_list.py

from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page


def build_payment_gateway_list_page(
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
        # 🔗 reference (order, invoice, dll)
        TableColumn(key="reference_type", label="Ref Type"),
        TableColumn(key="reference_id", label="Reference"),
        # 💰 amount
        TableColumn(
            key="amount",
            label="Amount",
            format="currency",
            align="right",
            weight="semibold",
        ),
        # 🌐 gateway
        TableColumn(key="provider", label="Provider"),
        TableColumn(key="channel", label="Channel"),
        # 🔑 external
        TableColumn(
            key="external_id",
            label="Gateway ID",
            size="xs",
            text_style="muted",
        ),
        # 🔄 status
        TableColumn(
            key="status",
            label="Status",
            align="center",
            weight="semibold",
            size="xs",
        ),
        # ⏱️ timestamps
        TableColumn(
            key="created_at",
            label="Created",
            format="datetime",
            size="xs",
            text_style="muted",
        ),
        TableColumn(
            key="paid_at",
            label="Paid",
            format="datetime",
            size="xs",
            text_style="success",
        ),
    ]

    return Page(
        key=key,
        entity="payment_gateway",
        domain=domain,
        path=path,
        title=title_page,
        subtitle=subtitle_page,
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                title="Payment Transactions",
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
                        permission="business.payment_gateway.view",
                    ),
                ],
                top_actions=[],
            )
        ],
    )
