# verticals/isp/ui/pages/dashboard/network_engineer_dashboard.py

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
        key="isp.network.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard",
        title="Network Engineer Dashboard",
        permissions=[IspPermission.NETWORK_DASHBOARD_VIEW], 
        description="Network Infrastructure Control Panel",
        data_source="/entities/isp/network.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Network Management",
                items=[
                    ShortcutItem(key="devices", label="Devices", icon="server", to="/network/devices"),
                    ShortcutItem(key="ip_pool", label="IP Pools", icon="globe", to="/network/ip-pools"),
                    ShortcutItem(key="bandwidth", label="Bandwidth Profiles", icon="activity", to="/network/bandwidth"),
                    ShortcutItem(key="topology", label="Topology", icon="share-2", to="/network/topology"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="online_devices", title="Online Devices", data_key="online_devices"),
                    StatBlock(key="active_sessions", title="Active Sessions", data_key="active_sessions"),
                    StatBlock(key="network_alerts", title="Active Alerts", data_key="network_alerts"),
                    StatBlock(key="avg_latency", title="Avg Latency", data_key="avg_latency", suffix="ms"),
                ],
            ),

            ListViewBlock(
                title="Recent Network Alerts",
                data_key="network_alerts_list",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="device_name"),
                    subtitle=ListFieldSchema(key="alert_type"),
                    description=ListFieldSchema(key="message"),
                    status=ListFieldSchema(key="severity"),
                ),
                permissions=[IspPermission.NETWORK_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)