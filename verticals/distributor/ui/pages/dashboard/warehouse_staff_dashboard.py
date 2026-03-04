# # verticals/distributor/ui/pages/dashboard/warehouse_staff_dashboard.py

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
        key="distributor.warehouse_staff.dashboard",
        entity="dashboard",
        domain="distributor",
        path="/dashboard/warehouse-staff",
        title="Warehouse Staff Dashboard",
        permissions=[DistributorPermission.WAREHOUSE_STAFF_DASHBOARD_VIEW], 
        description="Picking & Delivery Operations",
        data_source="/entities/distributor/warehouse_staff.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Warehouse Tasks",
                items=[
                    ShortcutItem(key="do_list", label="Delivery Order List", icon="truck", to="/sales/delivery-orders"),
                    ShortcutItem(key="picking", label="Picking List", icon="clipboard", to="/inventory/picking"),
                    ShortcutItem(key="stock_check", label="Stock Check", icon="archive", to="/inventory/stock"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="pending_do", title="Pending DO", data_key="pending_do"),
                    StatBlock(key="goods_receipt_today", title="Goods Receipt Today", data_key="goods_receipt_today"),
                ]
            ),

            ListViewBlock(
                title="DO Waiting Picking",
                data_key="do_waiting",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="do_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="delivery_date"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[DistributorPermission.WAREHOUSE_STAFF_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("distributor", UI_PAGES)