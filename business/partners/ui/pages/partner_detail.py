# business/partners/ui/pages/partner_detail.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    FormBlock,
    FileBlock,
    TagBlock,
    StatBlock,
    ContainerBlock,
    ActionBlock,
)
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="partners.detail",
    domain="business",
    entity="partners",
    path="/business/partners/:id/detail",
    title="Ustadz Detail",
    permissions=["business.partners.view"],
    data_source="/business/partners/{id}/",
    method="GET",
    blocks=[
        # ── Container Block untuk layout profil & info ringkas ──
        ContainerBlock(
            direction="row",
            gap=24,
            blocks=[
                # ── FileBlock untuk gallery foto ──
                FileBlock(
                    title="Foto Ustadz",
                    entity_type="partner",
                    entity_id_from="id",
                    multiple=True,
                    accept="image/*",
                    permissions=["business.partners.view"],
                ),
                
                # ── FormBlock read-only untuk profil dasar ──
                FormBlock(
                    type="form",
                    mode="view",
                    title="Profil Ustadz",
                    description="Informasi lengkap tentang ustadz",
                    fields=[
                        Field(key="name", label="Nama", type="text"),
                        Field(key="email", label="Email", type="email"),
                        Field(key="phone", label="Telepon", type="text"),
                        Field(key="address", label="Alamat", type="textarea"),
                        Field(key="notes", label="Catatan", type="textarea"),
                    ],
                    actions=[],
                ),
                # ── StatBlock untuk rating & tarif ──
                ContainerBlock(
                    direction="column",
                    gap=12,
                    blocks=[
                        StatBlock(
                            key="base_price",
                            title="Tarif / jam",
                            value=None,
                            type="stat",
                            meta={
                                "format": "currency", 
                                "currency": "IDR"
                            }
                        ),
                        StatBlock(
                            key="rating_avg",
                            title="Rating",
                            value=None,
                            type="stat",
                            meta={"suffix": "⭐"},
                            suffix="⭐",
                        ),
                        StatBlock(
                            key="rating_count",
                            title="Jumlah Review",
                            value=None,
                            type="stat",
                        ),
                    ],
                ),
            ],
        ),

        # ── TagBlock untuk bidang keahlian / skills ──
        TagBlock(
            title="Bidang Keahlian",
            entity_type="business_partners.partner",
            entity_id_from="id",
            allow_create=False,
            permissions=["business.partners.view"],
        ),

        # ── Jadwal tersedia (custom TableBlock / bisa ganti nanti ke ScheduleBlock) ──
        ContainerBlock(
            direction="column",
            blocks=[
                FormBlock(
                    title="Jadwal Tersedia",
                    mode="view",
                    fields=[
                        Field(key="available_schedule", label="Jadwal", type="textarea"),
                    ],
                )
            ],
        ),

        # ── Tombol Booking ──
        ContainerBlock(
            direction="row",
            justify="start",
            blocks=[
                ActionBlock(
                    title="",
                    actions=[
                        Action(
                            type="navigate",
                            label="Booking Sekarang",
                            icon="calendar",
                            to="/business/bookings/create?partner_id={id}",
                            permission="business.bookings.create",
                        )
                    ],
                    justify="center",
                )
            ],
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)