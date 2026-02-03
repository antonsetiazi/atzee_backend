# business/customers/ui/pages/customer_list.py
from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="customers.list",
    entity="customers",
    domain="business",
    title="Customers",
    permissions=["business.customers.view"],
    blocks=[
        TableBlock(
            data_source="/entities/business/customers.list/query/",
            search_mode="client",
            columns=[
                TableColumn(key="code", label="Code"),
                TableColumn(key="name", label="Name"),
                TableColumn(key="email", label="Email"),
                TableColumn(key="phone", label="Phone"),
                TableColumn(key="is_active", label="Active"),
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="edit",
                    to="/business/customers/{id}/edit",
                    permission="business.customers.update"
                ),
                Action(
                    type="delete",
                    label="Delete",
                    icon="delete",
                    permission="business.customers.delete",
                    confirm={
                        "title": "Delete Customer",
                        "message": "Are you sure you want to delete this customer?",
                        "level": "danger",
                    },
                    endpoint="/business/customers/{id}/"
                ),
            ],
            top_actions=[
                Action(
                    type="navigate",
                    label="Create Customer",
                    to="/business/customers/create",
                    permission="business.customers.add"
                )
            ],
        )
    ]
)
