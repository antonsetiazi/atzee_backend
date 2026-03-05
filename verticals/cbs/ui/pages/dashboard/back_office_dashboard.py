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

from verticals.cbs.enum.permissions import CbsPermission


UI_PAGES = [
    Page(
        key="cbs.back_office.dashboard",
        entity="dashboard",
        domain="cbs",
        path="/dashboard",
        title="Back Office Dashboard",
        permissions=[CbsPermission.BACK_OFFICE_DASHBOARD_VIEW],
        description="Reconciliation & Settlement",
        data_source="/entities/cbs/back_office.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Control",
                items=[
                    ShortcutItem(key="reversal", label="Reversal Approval", icon="rotate-ccw", to="/transactions/reversal"),
                    ShortcutItem(key="settlement", label="Interbranch Settlement", icon="shuffle", to="/treasury/settlement"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="pending_recon", title="Pending Reconciliation", data_key="pending_reconciliation"),
                    StatBlock(key="settlement_status", title="Settlement Status", data_key="settlement_status"),
                ]
            ),

            ListViewBlock(
                title="Unreconciled Transactions",
                data_key="unreconciled_transactions",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="reference_number"),
                    subtitle=ListFieldSchema(key="account_number"),
                    description=ListFieldSchema(key="amount"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[CbsPermission.BACK_OFFICE_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("cbs", UI_PAGES)