# verticals/distributor/ui/pages/dashboard/warehouse_manager_dashboard.py

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
        key="distributor.warehouse_manager.dashboard",
        entity="dashboard",
        domain="distributor",
        path="/dashboard/warehouse-manager",
        title="Warehouse Manager Dashboard",
        permissions=[DistributorPermission.WAREHOUSE_MANAGER_DASHBOARD_VIEW], 
        description="Inventory & Warehouse Overview",
        data_source="/entities/distributor/warehouse_manager.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Inventory Control",
                items=[
                    ShortcutItem(key="stock_overview", label="Stock Overview", icon="archive", to="/inventory/stock"),
                    ShortcutItem(key="stock_adjustment", label="Stock Adjustment", icon="sliders", to="/inventory/adjustment"),
                    ShortcutItem(key="stock_transfer", label="Stock Transfer", icon="repeat", to="/inventory/transfer"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="stock_value", title="Stock Value", data_key="stock_value"),
                    StatBlock(key="low_stock", title="Low Stock Alert", data_key="low_stock"),
                    StatBlock(key="fast_moving", title="Fast Moving Items", data_key="fast_moving"),
                ]
            ),

            ListViewBlock(
                title="Slow Moving Items",
                data_key="slow_moving_items",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="product_name"),
                    subtitle=ListFieldSchema(key="category"),
                    description=ListFieldSchema(key="stock_age"),
                ),
                permissions=[DistributorPermission.WAREHOUSE_MANAGER_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("distributor", UI_PAGES)