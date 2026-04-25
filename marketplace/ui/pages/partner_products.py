# marketplace/ui/pages/partner_products.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn, ActionBlock
from core.ui.schema.action import Action

from marketplace.enum.permissions import MarketplacePermission
 

UI_PAGES = Page(
    key="partner.products.list",
    entity="products",
    domain="marketplace",
    path="/partner/products",
    title="Layanan Saya",
    subtitle="Kelola layanan dan produk yang Anda tawarkan",
    permissions=[
        MarketplacePermission.PARTNER_PRODUCTS_VIEW
    ],
    data_source="/entities/marketplace/partner.products.list/query/",
    blocks=[
        TableBlock(
            title="Daftar Layanan",
            data_key="items",
            search_mode="server",

            columns=[
                TableColumn(
                    key="name",
                    label="Nama Layanan",
                ),

                TableColumn(
                    key="type",
                    label="Tipe",
                    align="center",
                ),

                TableColumn(
                    key="category_name",
                    label="Kategori",
                ),

                TableColumn(
                    key="price",
                    label="Harga",
                    format="currency",
                    align="right",
                ),

                TableColumn(
                    key="is_active",
                    label="Status",
                    align="center",
                ),

                TableColumn(
                    key="created_at",
                    label="Dibuat",
                    format="datetime",
                ),
            ],

            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="pencil",
                    to="/partner/products/{id}",
                    permission=MarketplacePermission.PARTNER_PRODUCTS_EDIT,
                )
            ],
        ),

        ActionBlock(
            title="",
            justify="center",
            align="center",
            actions=[
                Action(
                    type="navigate",
                    label="Tambah Layanan",
                    icon="plus",
                    to="/partner/products/create",
                    permission=MarketplacePermission.PARTNER_PRODUCTS_CREATE,
                )
            ],
        ),
    ],
)

register_ui_module_pages("marketplace", UI_PAGES)