# business/bookings/ui/pages/booking_payment.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import ContainerBlock, InfoBlock, ActionBlock
from core.ui.schema.action import Action
from business.enum.permissions import BusinessPermission


UI_PAGES = Page(
    key="bookings.payment",
    domain="business",
    entity="bookings",
    path="/business/bookings/:id/payment",
    title="Pembayaran Booking",
    permissions=[BusinessPermission.BOOKINGS_PAY],
    data_source="/business/bookings/{id}/",
    method="GET",
    blocks=[
        ContainerBlock(
            direction="column",
            gap=24,
            blocks=[
                InfoBlock(key="booking_number", title="Booking ID", value=None),
                InfoBlock(key="scheduled_at", title="Scheduled Date", value=None),
                InfoBlock(key="status", title="Booking Status", value=None),
                InfoBlock(key="total_price", title="Total", value=None, meta={"format": "currency", "currency": "IDR"}),
            ]
        ),
        ContainerBlock(
            direction="row",
            justify="start",
            blocks=[
                ActionBlock(
                    title="",
                    actions=[
                        Action(
                            type="api",
                            label="Bayar dengan Wallet",
                            key="pay_with_wallet",
                            endpoint="/wallets/pay-booking/{id}/",  # endpoint API baru
                            affects="reload",
                            success_title="Pembayaran Berhasil",
                            success_message="Booking telah dikonfirmasi dan saldo wallet dipotong.",
                            confirm={
                                "title": "Konfirmasi Pembayaran",
                                "message": "Saldo wallet akan dipotong dan booking akan dikunci.",
                                "level": "warning",
                            },
                            permission="business.bookings.pay",
                            when={"status": "PENDING_PAYMENT"},
                        )
                    ],
                    justify="center",
                )
            ],
        ),
    ]
)

register_ui_module_pages("business", UI_PAGES)