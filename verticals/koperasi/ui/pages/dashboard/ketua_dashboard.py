# verticals/koperasi/ui/pages/dashboard/ketua_dashboard.py

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

from verticals.koperasi.enum.permissions import KoperasiPermission


UI_PAGES = [
    Page(
        key="koperasi.ketua.dashboard",
        entity="dashboard",
        domain="koperasi",
        path="/dashboard",
        title="Ketua Dashboard",
        permissions=[KoperasiPermission.KETUA_DASHBOARD_VIEW], 
        description="Full Cooperative Governance Overview",
        data_source="/entities/koperasi/ketua.dashboard/query/",
        blocks=[

            # QUICK ACCESS
            ShortcutBlock(
                title="Governance Control",
                items=[
                    ShortcutItem(key="approve_member", label="Approve Member", icon="user-check", to="/members/approval"),
                    ShortcutItem(key="loan_approval", label="Loan Approval", icon="check-circle", to="/loans/approval"),
                    ShortcutItem(key="generate_shu", label="Generate SHU", icon="percent", to="/shu/generate"),
                    ShortcutItem(key="rat_period", label="RAT Period", icon="calendar", to="/rat"),
                ],
            ),

            # KPI
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="total_members", title="Total Members", data_key="total_members"),
                    StatBlock(key="total_savings", title="Total Savings", data_key="total_savings"),
                    StatBlock(key="active_loans", title="Active Loans", data_key="active_loans"),
                    StatBlock(key="shu_current", title="Current SHU Pool", data_key="shu_pool"),
                ]
            ),

            # RECENT LOAN REQUEST
            ListViewBlock(
                title="Pending Loan Approvals",
                data_key="pending_loans",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="member_name"),
                    subtitle=ListFieldSchema(key="loan_amount"),
                    description=ListFieldSchema(key="tenor"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[KoperasiPermission.KETUA_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("koperasi", UI_PAGES)