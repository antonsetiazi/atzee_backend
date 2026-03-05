# verticals/cbs/ui/pages/dashboard/compliance_dashboard.py

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
        key="cbs.compliance.dashboard",
        entity="dashboard",
        domain="cbs",
        path="/dashboard",
        title="Compliance Dashboard",
        permissions=[CbsPermission.COMPLIANCE_DASHBOARD_VIEW],
        description="AML & Regulatory Monitoring",
        data_source="/entities/cbs/compliance.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Compliance Tools",
                items=[
                    ShortcutItem(key="str", label="STR Report", icon="alert-circle", to="/compliance/str"),
                    ShortcutItem(key="ctr", label="CTR Report", icon="file-text", to="/compliance/ctr"),
                    ShortcutItem(key="sanction", label="Sanction Check", icon="shield", to="/compliance/sanction"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="flagged_transactions", title="Flagged Transactions", data_key="flagged_transactions"),
                    StatBlock(key="high_risk_customers", title="High Risk Customers", data_key="high_risk_customers"),
                ]
            ),

            ListViewBlock(
                title="Suspicious Activities",
                data_key="suspicious_activities",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="reference_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="amount"),
                    status=ListFieldSchema(key="risk_level"),
                ),
                permissions=[CbsPermission.COMPLIANCE_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("cbs", UI_PAGES)