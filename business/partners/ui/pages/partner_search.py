# business/partners/ui/pages/partner_search.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    FormBlock,
    CardListBlock,
    CardField,
    ContainerBlock,
    # TableColumn,
)
from core.ui.schema.field import Field
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="partners.search",
    entity="partners",
    domain="business",
    title="Search Partners",
    path="/business/partners/search",
    permissions=["business.partners.view"],
    data_source="/entities/business/partners.search/query/",
    method="POST",
    blocks=[
        ContainerBlock(
            direction="row",
            gap=24,
            blocks=[
                FormBlock(
                    mode="filter",
                    submit_to="/entities/business/partners.search/query/",
                    method="POST",
                    title="Search Filters",
                    description="Filter partners by keyword, rating, price or location",
                    fields=[
                        Field(
                            key="keyword",
                            label="Keyword",
                            type="text",
                        ),
                        Field(
                            key="min_rating",
                            label="Minimum Rating",
                            type="number",
                        ),
                        Field(
                            key="max_price",
                            label="Maximum Price",
                            type="number",
                        ),
                        Field(
                            key="latitude",
                            label="Latitude",
                            type="number",
                        ),
                        Field(
                            key="longitude",
                            label="Longitude",
                            type="number",
                        ),
                        Field(
                            key="radius_km",
                            label="Radius (KM)",
                            type="number",
                        ),
                    ],
                    actions=[
                        Action(type="submit", label="Search"),
                    ],
                ),
                CardListBlock(
                    title="Search Results",
                    layout="grid",
                    columns=2,
                    selectable="none",
                    value_key="id",
                    data_key="items",
                    fields=[
                        CardField(key="image_url", label="Image"),
                        CardField(key="name", label="Name"),
                        CardField(key="base_price", label="Base Price", format="currency"),
                        CardField(key="rating_avg", label="Rating"),
                    ],
                    permissions="business.partners.view",
                    item_action=Action(
                        type="navigate",
                        label="View Detail",
                        to="/business/partners/{id}/detail",
                        permission="business.partners.view",
                    ),
                )
            ]
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)