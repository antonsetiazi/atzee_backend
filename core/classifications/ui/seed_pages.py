# core/classifications/ui/seed_pages.py

from core.classifications.categories.ui.pages import UI_PAGES as CATEGORY_PAGES
from core.classifications.tags.ui.pages import UI_PAGES as TAG_PAGES 

UI_PAGES = [
    *CATEGORY_PAGES,
    *TAG_PAGES
]
