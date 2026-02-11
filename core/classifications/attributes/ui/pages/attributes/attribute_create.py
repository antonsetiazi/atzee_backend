# core/classifications/attributes/ui/pages/attributes/attribute_create.py

from ._base_attribute_form import (
    build_attribute_form_page,
)

UI_PAGES = build_attribute_form_page(
    key="attributes.create",
    domain="core",
    path="/settings/classifications/attributes/create",
    submit_to="/attributes/",
    method="POST",
    permissions=["core.attributes.add"],
    title="Create Attribute",
    redirect_page="/settings/classifications/attributes",
)
