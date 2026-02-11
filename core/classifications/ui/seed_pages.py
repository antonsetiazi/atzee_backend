# core/classifications/ui/seed_pages.py

from core.classifications.categories.ui.pages import UI_PAGES as CATEGORY_PAGES
from core.classifications.tags.ui.pages import UI_PAGES as TAG_PAGES 
from core.classifications.labels.ui.pages import UI_PAGES as LABEL_PAGES 
from core.classifications.attributes.ui.pages.attributes import UI_PAGES as ATTRIBUTE_PAGES
from core.classifications.attributes.ui.pages.attribute_options import UI_PAGES as ATTRIBUTE_OPTION_PAGES

UI_PAGES = [
    *CATEGORY_PAGES,
    *TAG_PAGES,
    *LABEL_PAGES,
    *ATTRIBUTE_PAGES,
    *ATTRIBUTE_OPTION_PAGES
]
