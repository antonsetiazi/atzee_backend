# business/customers/ui/pages/customer_create.py
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="customers.create",
    entity="customers",
    title="Customer",
    permissions=["business.customers.add"],
    blocks=[
        FormBlock(
            submit_to="/business/customers/",
            method="POST",
            title="Create Customer",
            description="Lengkapi data customer dengan benar",
            fields=[
                Field(key="code", label="Customer Code", type="text"),
                Field(key="name", label="Customer Name", type="text", required=True),
                Field(key="email", label="Email", type="email"),
                Field(key="phone", label="Phone", type="text"),
                Field(key="address", label="Address", type="textarea"),
                Field(key="notes", label="Notes", type="textarea"),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(type="redirect", label="Cancel", to="/customers")
            ]
        )
    ],
)
