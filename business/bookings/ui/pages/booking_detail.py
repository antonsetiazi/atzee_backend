# business/bookings/ui/pages/booking_detail.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    InfoBlock,
    CardField,
    WorkflowBlock,
    WorkflowStatus,
    CardListBlock,
)
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="bookings.detail",
    domain="business",
    entity="bookings",
    path="/business/bookings/:id/detail",
    title="Detail Booking",
    permissions=["business.bookings.view"],
    data_source="/business/bookings/{id}/",
    method="GET",
    blocks=[
        # HEADER
        ContainerBlock(
            direction="row",
            gap=24,
            blocks=[
                InfoBlock(key="booking_number", title="Booking ID", value=None),
                InfoBlock(key="scheduled_at", title="Scheduled Date", value=None),
                InfoBlock(key="status", title="Booking Status", value=None),
            ],
            background_color="bg-white"
        ),

        # BODY: list layanan / items
        CardListBlock(
            title="Services / Items",
            data_key="items",
            permissions=["business.bookings.view"],
            fields=[
                CardField(key="product_name", label="Service"),
                CardField(key="quantity", label="Qty"),
                CardField(
                    key="unit_price", 
                    label="Unit Price", 
                    meta={
                        "format": "currency", 
                        "currency": "IDR"
                    }
                ),
                CardField(
                    key="subtotal", 
                    label="Subtotal", 
                    meta={
                        "format": "currency", 
                        "currency": "IDR"
                    }
                ),
            ],
        ),

        # FOOTER
        ContainerBlock(
            direction="row",
            gap=24,
            blocks=[
                InfoBlock(
                    key="subtotal_amount", 
                    title="Subtotal", 
                    value=None,  
                    meta={
                        "format": "currency", 
                        "currency": "IDR"
                    }
                ),
                InfoBlock(
                    key="platform_fee", 
                    title="Platform Fee", 
                    value=None, 
                    meta={
                        "format": "currency", 
                        "currency": "IDR"
                    }
                ),
                InfoBlock(
                    key="total_price", 
                    title="Total", 
                    value=None, 
                    meta={
                        "format": "currency", 
                        "currency": "IDR"
                    }
                ),
            ],
            background_color="bg-white"
        ),

        WorkflowBlock(
            status=WorkflowStatus(
                key="status",
                label="Status Booking",
            ),
            actions=[
                Action(
                    key="pay",
                    type="navigate",
                    label="Bayar Sekarang",
                    to="/business/bookings/{id}/payment/",
                    when={"status": "PENDING_PAYMENT"},
                    permission="business.bookings.view",
                ),
                Action(
                    key="complete",
                    type="navigate",
                    label="Selesaikan",
                    to="/business/bookings/{id}/complete/",
                    when={"status": "confirmed"},
                    permission="business.bookings.view",
                ),
                Action(
                    key="cancel",
                    type="delete",
                    label="Batalkan",
                    endpoint="/business/bookings/{id}/cancel/",
                    confirm={
                        "title": "Batalkan Booking?",
                        "message": "Booking akan dibatalkan permanen.",
                        "level": "danger",
                    },
                    when={"status__in": ["draft", "confirmed"]},
                    permission="business.bookings.view",
                ),
            ]
        )
    ]
)

register_ui_module_pages("business", UI_PAGES)