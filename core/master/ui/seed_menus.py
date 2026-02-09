# core/master/ui/seed_menus.py

from core.master.ui.menus import UI_MENUS as MASTER_MENUS
from core.master.currencies.ui.menus import UI_MENUS as CURRENCY_MENUS
from core.master.uom.ui.menus import UI_MENUS as UOM_MENUS
from core.master.locations.ui.menus import UI_MENUS as LOCATIONS_MENUS

UI_MENUS = (
    MASTER_MENUS +
    CURRENCY_MENUS +
    UOM_MENUS +
    LOCATIONS_MENUS
)
