# business/customers/ui/pages/customer_edit.py

from core.ui.schema.field import Field
from business.customers.ui.pages._base_customer_form import (
    build_customer_form_page,
)

UI_PAGES = build_customer_form_page(
    key="customers.edit",
    domain="business",
    path="/business/customers/:id/edit",
    submit_to="/business/customers/{id}/",
    method="PATCH",
    permissions=["business.customers.update"],
    title="Edit Customer",
    redirect_page="/business/customers",
    extra_fields=[
        Field(
            key="id",
            label="Customer ID",
            type="hidden",
        ),
    ],
)
