# core/classifications/ui/seed_menus.py

from core.classifications.ui.menus import UI_MENUS as CLASSIFICATION_MENUS
from core.classifications.categories.ui.menus import UI_MENUS as CATEGORY_MENUS
from core.classifications.tags.ui.menus import UI_MENUS as TAG_MENUS


UI_MENUS = (
    CLASSIFICATION_MENUS +
    CATEGORY_MENUS + 
    TAG_MENUS
)
