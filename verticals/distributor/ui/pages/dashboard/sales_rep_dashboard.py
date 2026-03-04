# verticals/distributor/ui/pages/dashboard/sales_rep_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock, StatBlock,
    ShortcutBlock, ShortcutItem,
    ListViewBlock, ListFieldSchema, ListTileSchema,
)

from verticals.distributor.enum.permissions import DistributorPermission


UI_PAGES = [
    Page(
        key="distributor.sales_rep.dashboard",
        entity="dashboard",
        domain="distributor",
        path="/dashboard/sales-rep",
        title="My Sales Dashboard",
        permissions=[DistributorPermission.SALES_REP_DASHBOARD_VIEW], 
        description="Field Sales Activity",
        data_source="/entities/distributor/sales_rep.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Access",
                items=[
                    ShortcutItem(key="create_so", label="Create Sales Order", icon="plus-circle", to="/sales/orders/create"),
                    ShortcutItem(key="customer_list", label="Customer List", icon="users", to="/customers"),
                    ShortcutItem(key="visit_log", label="Visit Log", icon="map-pin", to="/sales/visit-log"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="my_target", title="My Target", data_key="my_target"),
                    StatBlock(key="achievement", title="Achievement", data_key="achievement", suffix="%"),
                    StatBlock(key="outstanding_customer", title="Outstanding Customer", data_key="outstanding_customer"),
                ]
            ),

            ListViewBlock(
                title="My Recent Orders",
                data_key="recent_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="order_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="total_amount"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[DistributorPermission.SALES_REP_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("distributor", UI_PAGES)