# core/master/locations/ui/pages/__init__.py

from .location_list import UI_PAGES as LOCATION_LIST_PAGE
from .location_create import UI_PAGES as LOCATION_CREATE_PAGE
from .location_edit import UI_PAGES as LOCATION_EDIT_PAGE

UI_PAGES = [
    LOCATION_LIST_PAGE,
    LOCATION_CREATE_PAGE,
    LOCATION_EDIT_PAGE,
]
