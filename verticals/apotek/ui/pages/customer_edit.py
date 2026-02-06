# verticals/apotek/ui/pages/customer_edit.py

from core.ui.schema.field import Field
from business.customers.ui.pages._base_customer_form import (
    build_customer_form_page,
)

UI_PAGES = build_customer_form_page(
    key="apotek.customers.edit",
    domain="business",
    path="/apotek/customers/:id/edit",
    submit_to="/business/customers/{id}/",
    method="PATCH",
    permissions=["business.customers.update"],
    title="Edit Customer",
    redirect_page="/apotek/customers",
    extra_fields=[
        Field(
            key="id",
            label="Customer ID",
            type="hidden",
        ),
        Field(
            key="extensions.apotek.medical_note",
            label="Medical Note",
            type="textarea",
        ),
        Field(
            key="extensions.apotek.allergies",
            label="Allergies",
            type="textarea",
        ),
        Field(
            key="extensions.apotek.requires_prescription",
            label="Requires Prescription",
            type="boolean",
        ),
    ],
)
