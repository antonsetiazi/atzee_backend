# verticals/koperasi/ui/pages/dashboard/pengawas_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.koperasi.enum.permissions import KoperasiPermission


UI_PAGES = [
    Page(
        key="koperasi.pengawas.dashboard",
        entity="dashboard",
        domain="koperasi",
        path="/dashboard",
        title="Pengawas Dashboard",
        permissions=[KoperasiPermission.PENGAWAS_DASHBOARD_VIEW], 
        description="Audit & Monitoring Overview",
        data_source="/entities/koperasi/pengawas.dashboard/query/",
        blocks=[

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="total_assets", title="Total Assets", data_key="total_assets"),
                    StatBlock(key="loan_ratio", title="Loan Ratio", data_key="loan_ratio", suffix="%"),
                    StatBlock(key="shu_projection", title="SHU Projection", data_key="shu_projection"),
                ]
            ),

            ListViewBlock(
                title="Recent Audit Logs",
                data_key="audit_logs",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="action"),
                    subtitle=ListFieldSchema(key="user"),
                    description=ListFieldSchema(key="timestamp"),
                ),
                permissions=[KoperasiPermission.PENGAWAS_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("koperasi", UI_PAGES)