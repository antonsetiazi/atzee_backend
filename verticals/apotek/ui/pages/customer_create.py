# verticals/apotek/ui/pages/customer_create.py

from core.ui.schema.field import Field

from business.customers.ui.pages._base_customer_form import (
    build_customer_form_page,
)

UI_PAGES = build_customer_form_page(
    key="apotek.customers.create",
    domain="business",
    path="/apotek/customers/create",
    submit_to="/business/customers/",
    method="POST",
    permissions=["business.customers.add"],
    title="Create Customer",
    redirect_page="/apotek/customers",
    extra_fields=[
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