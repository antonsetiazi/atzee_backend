# ==========================================================
# FILE: marketplace/ui/pages/partner_product_edit.py
# ==========================================================

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from marketplace.enum.permissions import MarketplacePermission


UI_PAGES = Page(
    key="partner.products.edit",
    entity="products",
    domain="marketplace",
    title="Edit Layanan",
    path="/partner/products/{id}",
    permissions=[
        MarketplacePermission.PARTNER_PRODUCTS_EDIT
    ],
    data_source="/entities/marketplace/partner.products.detail/query/",
    method="POST",
    blocks=[
        FormBlock(
            title="Edit Layanan",
            description="Perbarui data layanan atau produk Anda",
            mode="edit",
            submit_to="/entities/marketplace/partner.products.update/execute/",
            method="POST",
            redirect_to={
                "page": "/partner/products"
            },
            refresh_cache=[
                "partner.products.list",
                "partner.products.edit"
            ],
            fields=[
                Field(
                    key="id",
                    label="ID",
                    type="hidden",
                ),

                Field(
                    key="code",
                    label="Kode",
                    type="text",
                    required=True,
                ),

                Field(
                    key="name",
                    label="Nama Layanan",
                    type="text",
                    required=True,
                ),

                Field(
                    key="type",
                    label="Tipe",
                    type="select",
                    required=True,
                    options=[
                        {"value": "service", "label": "Service"},
                        {"value": "product", "label": "Product"},
                    ],
                ),

                Field(
                    key="category_id",
                    label="Kategori",
                    type="select",
                    data_source="/entities/core/categories.select.list/query/",
                    params={
                        "scope": "partners.service_category"
                    }
                ),

                Field(
                    key="price",
                    label="Harga",
                    type="number",
                ),

                Field(
                    key="duration_minutes",
                    label="Durasi (menit)",
                    type="number",
                ),

                Field(
                    key="stock",
                    label="Stok",
                    type="number",
                ),

                Field(
                    key="is_active",
                    label="Aktif",
                    type="boolean",
                ),
            ],

            actions=[
                Action(
                    type="submit",
                    label="Update",
                    icon="save",
                ),
                Action(
                    type="redirect",
                    label="Batal",
                    to="/partner/products",
                ),
            ],
        )
    ],
)

register_ui_module_pages("marketplace", UI_PAGES)