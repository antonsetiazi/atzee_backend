# business/customers/ui/pages/customer_edit.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="customers.edit",
    entity="customers",
    domain="business",
    title="Customer",
    permissions=["business.customers.update"],
    blocks=[
        FormBlock(
            submit_to="/business/customers/{id}/",  # gunakan placeholder id
            method="PATCH",
            title="Edit Customer",
            description="Lengkapi data customer dengan benar",
            redirect_to={
                "page": "customers.list",
            },
            fields=[
                Field(key="id", label="Customer ID", type="hidden"),
                Field(key="code", label="Customer Code", type="text"),
                Field(key="name", label="Customer Name", type="text", required=True),
                Field(key="email", label="Email", type="email"),
                Field(key="phone", label="Phone", type="text"),
                Field(key="address", label="Address", type="textarea"),
                Field(key="notes", label="Notes", type="textarea"),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(type="redirect", label="Cancel", to="/business/customers"),
            ],
        )
    ],
)
