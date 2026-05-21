# marketplace/ui/pages/partner_products.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page
from marketplace.enum.permissions import MarketplacePermission

UI_PAGES = Page(
    key="partner.products.list",
    entity="products",
    domain="marketplace",
    path="/partner/products",
    title="Layanan Saya",
    subtitle="Kelola layanan dan produk yang Anda tawarkan",
    permissions=[MarketplacePermission.PARTNER_PRODUCTS_VIEW],
    data_source="/entities/marketplace/partner.products.list/query/",
    actions=[
        Action(
            type="navigate",
            label="Tambah Layanan",
            icon="plus",
            to="/partner/products/create",
            permission=MarketplacePermission.PARTNER_PRODUCTS_CREATE,
        )
    ],
    blocks=[
        TableBlock(
            title="Daftar Layanan",
            data_key="items",
            on_row_click="/partner/products/{id}",
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
                    boolean_style="active_inactive",
                    size="xs",
                    weight="semibold",
                ),
                TableColumn(
                    key="created_at",
                    label="Dibuat",
                    format="datetime",
                    size="xs",
                    text_style="muted",
                ),
            ],
        ),
    ],
)

register_ui_module_pages("marketplace", UI_PAGES)
