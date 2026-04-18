# core/wallet_withdrawal/ui/pages/withdrawal_approve.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission


UI_PAGES = Page(
    key="withdrawals.approve",
    entity="withdrawals",
    domain="core",

    title="Approval Withdrawal",
    path="/admin/withdrawals/approve/{id}",

    permissions=[
        CorePermission.ADMIN_WALLET_WITHDRAWAL_VIEW
    ],

    data_source="/entities/core/withdrawals.detail/query/",

    blocks=[
        FormBlock(
            title="Approval Withdrawal",
            description="Review dan tentukan status withdrawal",

            mode="edit",

            submit_to="/entities/core/withdrawals.approval/execute/",
            method="POST",

            redirect_to={
                "page": "/admin/withdrawals"
            },

            refresh_cache=[
                "withdrawals.list",
                "withdrawals.approve",
            ],

            fields=[
                # hidden id
                Field(
                    key="id",
                    label="ID",
                    type="hidden",
                ),

                # readonly info
                Field(
                    key="user_name",
                    label="User",
                    type="text",
                    disabled=True,
                ),
                Field(
                    key="user_phone",
                    label="Phone",
                    type="text",
                    disabled=True,
                ),
                Field(
                    key="amount",
                    label="Amount",
                    type="number",
                    disabled=True,
                ),
                Field(
                    key="fee",
                    label="Fee",
                    type="number",
                    disabled=True,
                ),
                Field(
                    key="net_amount",
                    label="Net Amount",
                    type="number",
                    disabled=True,
                ),
                Field(
                    key="destination_label",
                    label="Destination",
                    type="text",
                    disabled=True,
                ),
                Field(
                    key="status",
                    label="Current Status",
                    type="text",
                    disabled=True,
                ),

                # 🔥 decision field
                Field(
                    key="decision",
                    label="Decision",
                    type="select",
                    required=True,
                    options=[
                        {
                            "label": "Approve",
                            "value": "approve",
                        },
                        {
                            "label": "Reject",
                            "value": "reject",
                        },
                    ],
                ),

                # optional reason
                Field(
                    key="reason",
                    label="Reason / Note",
                    type="textarea",
                ),
            ],

            actions=[
                Action(
                    type="submit",
                    label="Submit Approval",
                    icon="save",
                ),
                Action(
                    type="redirect",
                    label="Batal",
                    to="/admin/withdrawals",
                ),
            ],
        )
    ],
)

register_ui_module_pages("core", UI_PAGES)