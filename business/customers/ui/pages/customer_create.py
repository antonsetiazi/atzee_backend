# business/customers/ui/pages/customer_create.py

from business.customers.ui.pages._base_customer_form import (
    build_customer_form_page,
)

UI_PAGES = build_customer_form_page(
    key="customers.create",
    domain="business",
    path="/business/customers/create",
    submit_to="/business/customers/",
    method="POST",
    permissions=["business.customers.add"],
    title="Create Customer",
    redirect_page="/business/customers",
)