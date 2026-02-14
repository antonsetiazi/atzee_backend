# core/widgets/types/banner.py

from core.ui.schema.field import Field

def banner_fields() -> list[Field]:
    return [
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
            required=False,
            default=True,
        ),
    ]
