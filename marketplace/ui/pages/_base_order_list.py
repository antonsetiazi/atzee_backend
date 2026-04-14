# marketplace/ui/pages/_base_order_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action

from marketplace.enum.permissions import MarketplacePermission

def build_order_list_page(
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
        TableColumn(key="order_number", label="Order No"),

        # 👤 USER
        TableColumn(key="user_name", label="User"),
        TableColumn(key="user_phone", label="Phone"),

        # 🤝 PARTNER
        TableColumn(key="partner_name", label="Partner"),

        # 📦 fulfillment
        TableColumn(key="fulfillment_type", label="Type"),

        # 💰 amount
        TableColumn(
            key="total_amount",
            label="Total",
            format="currency",
            align="right",
        ),

        # 💳 payment
        TableColumn(
            key="payment_status",
            label="Payment",
            align="center",
        ),

        # 🔄 order status
        TableColumn(
            key="status",
            label="Status",
            align="center",
        ),

        # ⏱️ created
        TableColumn(
            key="created_at",
            label="Created",
            format="datetime",
        ),
    ]

    return Page(
        key=key,
        entity="orders",
        domain=domain,
        path=path,
        title=title_page,
        subtitle=subtitle_page,
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                title="Order List",
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
                        permission=MarketplacePermission.ADMIN_ORDERS_VIEW,
                    ),
                ],
                top_actions=[],
            )
        ],
    )