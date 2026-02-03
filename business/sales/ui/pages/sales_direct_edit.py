# business/sales/pages/sales_direct_edit.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="sales.direct.edit",
    entity="sales.direct",
    domain="business",
    title="Direct Sales",
    permissions=["business.sales.update"],
    blocks=[
        FormBlock(
            mode="create",
            submit_to="/business/transactions/{id}/",
            method="PATCH",
            title="Edit Direct Sales",
            description="Perbarui data penjualan langsung",
            redirect_to={
                "page": "sales.direct.detail",
                "param": "id",        # ambil dari response.id
            },
            fields=[
                Field(key="transaction_date", label="Date", type="date", required=True),
                Field(
                    key="customer_id",
                    label="Customer",
                    type="select",
                    data_source={
                        "type": "entity",
                        "domain": "business",
                        "entity": "customers.list",
                        "query": {
                            "filters": {
                                "is_active": True
                            },
                            "fields": ["id", "code", "name"]
                        },
                        "map": {
                            "value": "id",
                            "label": "{code} - {name}"
                        }
                    },
                    required=False,
                ),
                Field(key="notes", label="Notes", type="textarea"),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(
                    type="redirect",
                    label="Cancel",
                    to="/business/sales/direct",
                ),
            ],
        )
    ],
)
