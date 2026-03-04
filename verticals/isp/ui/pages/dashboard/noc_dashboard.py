# verticals/isp/ui/pages/dashboard/noc_dashboard.py

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

from verticals.isp.enum.permissions import IspPermission


UI_PAGES = [
    Page(
        key="isp.noc.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard/noc",
        title="NOC Dashboard",
        permissions=[IspPermission.NOC_DASHBOARD_VIEW],
        description="Live Network Monitoring & Alerts",
        data_source="/entities/isp/noc.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Network Actions",
                items=[
                    ShortcutItem(key="monitoring", label="Monitoring", icon="activity", to="/network/monitoring"),
                    ShortcutItem(key="sessions", label="Active Sessions", icon="wifi", to="/network/sessions"),
                    ShortcutItem(key="tickets", label="Trouble Tickets", icon="life-buoy", to="/operations/tickets"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="live_alerts", title="Active Alerts", data_key="active_alerts"),
                    StatBlock(key="down_devices", title="Down Devices", data_key="down_devices"),
                    StatBlock(key="active_sessions", title="Active Sessions", data_key="active_sessions"),
                    StatBlock(key="sla_risk", title="SLA At Risk", data_key="sla_risk"),
                ],
            ),

            ListViewBlock(
                title="Latest Network Alerts",
                data_key="recent_alerts",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="device_name"),
                    subtitle=ListFieldSchema(key="alert_type"),
                    description=ListFieldSchema(key="message"),
                    status=ListFieldSchema(key="severity"),
                ),
                permissions=[IspPermission.NOC_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)