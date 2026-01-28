# business/customers/ui/pages/customer_list.py
from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="customers.list",
    entity="customers",
    title="Customers",
    permissions=["business.customers.view"],
    blocks=[
        TableBlock(
            data_source="/business/customers/",
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
                    to="/customers/{id}/edit",
                    permission="business.customers.update"
                ),
                Action(
                    type="delete",
                    label="Delete",
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
                    to="/customers/create",
                    permission="business.customers.add"
                )
            ]
        )
    ]
)

# UI_PAGES = {
#     "key": "customers.list",
#     "entity": "customers",
#     "title": "Customers",
#     "permissions": ["business.customers.view"],
#     "blocks": [
#         {
#             "type": "table",
#             "data_source": "/business/customers/",
#             "columns": [
#                 {"key": "code", "label": "Code"},
#                 {"key": "name", "label": "Name"},
#                 {"key": "email", "label": "Email"},
#                 {"key": "phone", "label": "Phone"},
#                 {"key": "is_active", "label": "Active"},
#             ],
#             "actions": [
#                 {
#                     "type": "navigate",
#                     "label": "Edit",
#                     "to": "/customers/{id}/edit",
#                     "permission": "business.customers.update",
#                 },
#                 {
#                     "type": "delete",
#                     "label": "Delete",
#                     "permission": "business.customers.delete",
#                     "confirm_message": "Are you sure you want to delete this customer?",
#                     "endpoint": "/business/customers/{id}/",  # placeholder id
#                 }
#             ],
#             "top_actions": [
#                 {
#                     "type": "navigate",
#                     "label": "Create Customer",
#                     "to": "/customers/create",
#                     "permission": "business.customers.add",
#                 }
#             ]
#         }
#     ],
# }
