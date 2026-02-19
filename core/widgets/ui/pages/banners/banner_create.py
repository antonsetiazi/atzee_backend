
from core.ui.registry import register_ui_module_pages
from core.widgets.ui.pages._base_widget_form import build_widget_form_page
from core.ui.schema.field import Field

UI_PAGES = build_widget_form_page(
    key="widgets.banners.create",
    domain="core",
    path="/widgets/banners/create",
    title_page="Banner",
    submit_to="/widgets/",
    method="POST",
    permissions=["core.widgets.add"],
    title="Create Banner",
    redirect_page="/widgets/banners",
    widget_type="banner",
    extra_fields=[
        Field(
            key="config.image_url",
            label="Image URL",
            type="text",
            required=True,
        ),
        Field(
            key="config.link_url",
            label="Link URL",
            type="text",
            required=False,
        ),
        Field(
            key="config.open_in_new_tab",
            label="Open In New Tab",
            type="boolean",
            default=True,
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)