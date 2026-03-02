# verticals/pos/ui/pages/dashboard/supervisor_dashboard.py

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

from verticals.pos.enum.permissions import PosPermission


UI_PAGES = [
    Page(
        key="pos.supervisor.dashboard",
        entity="dashboard",
        domain="pos",
        path="/dashboard",
        title="Shift Supervisor Dashboard",
        permissions=[PosPermission.SUPERVISOR_DASHBOARD_VIEW],
        description="Operational Control & Approval Center",
        data_source="/entities/pos/supervisor.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Operations",
                items=[
                    ShortcutItem(key="new_sale", label="New Sale", icon="shopping-cart", to="/pos/sale/new"),
                    ShortcutItem(key="shift_mgmt", label="Shift Management", icon="clock", to="/pos/shift/manage"),
                    ShortcutItem(key="refund", label="Refund / Void Approval", icon="shield", to="/pos/refund/approval"),
                    ShortcutItem(key="transactions", label="Transactions", icon="file-text", to="/pos/transactions"),
                ],
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="open_shifts", title="Open Shifts", data_key="open_shifts"),
                    StatBlock(key="pending_void", title="Pending Void", data_key="pending_void"),
                    StatBlock(key="refund_requests", title="Refund Requests", data_key="refund_requests"),
                    StatBlock(key="cash_over_short", title="Cash Over/Short", data_key="cash_variance"),
                ]
            ),

            ListViewBlock(
                title="Cashier Activity",
                data_key="cashier_activity",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="cashier_name"),
                    subtitle=ListFieldSchema(key="shift_status"),
                    description=ListFieldSchema(key="sales_total"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[PosPermission.SUPERVISOR_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("pos", UI_PAGES)