# core/classifications/ui/seed_menus.py

from core.classifications.ui.menus import UI_MENUS as CLASSIFICATION_MENUS
from core.classifications.categories.ui.menus import UI_MENUS as CATEGORY_MENUS
# from core.classifications.regions.ui.menus import UI_MENUS as REGION_MENUS
# from core.classifications.timezones.ui.menus import UI_MENUS as TIMEZONE_MENUS


UI_MENUS = (
    CLASSIFICATION_MENUS +
    CATEGORY_MENUS 
    # REGION_MENUS +
    # TIMEZONE_MENUS
)
