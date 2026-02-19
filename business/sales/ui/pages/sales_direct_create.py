# business/sales/ui/pages/sales_direct_create.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="sales.direct.create",
    entity="sales.direct",
    domain="business",
    path="/business/sales/direct/create",
    title="Direct Sales",
    permissions=["business.sales.add"],
    blocks=[
        FormBlock(
            mode="create",
            submit_to="/business/transactions/",
            method="POST",
            title="Create Direct Sales",
            description="Input transaksi penjualan langsung",
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

register_ui_module_pages("business", UI_PAGES)