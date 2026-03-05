# verticals/cbs/ui/pages/dashboard/auditor_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.cbs.enum.permissions import CbsPermission


UI_PAGES = [
    Page(
        key="cbs.auditor.dashboard",
        entity="dashboard",
        domain="cbs",
        path="/dashboard",
        title="Auditor Dashboard",
        permissions=[CbsPermission.AUDITOR_DASHBOARD_VIEW],
        description="Audit & Risk Monitoring",
        data_source="/entities/cbs/auditor.dashboard/query/",
        blocks=[

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_transactions", title="Total Transactions", data_key="total_transactions"),
                    StatBlock(key="risk_flags", title="Risk Flags", data_key="risk_flags"),
                ]
            ),

            ListViewBlock(
                title="Recent Journal Entries",
                data_key="recent_journals",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="journal_number"),
                    subtitle=ListFieldSchema(key="description"),
                    description=ListFieldSchema(key="amount"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[CbsPermission.AUDITOR_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("cbs", UI_PAGES)