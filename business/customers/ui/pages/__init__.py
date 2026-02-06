# business/customers/ui/pages/__init__.py

from .customer_list import UI_PAGES as CUSTOMER_LIST_PAGE
from .customer_create import UI_PAGES as CUSTOMER_CREATE_PAGE
from .customer_edit import UI_PAGES as CUSTOMER_EDIT_PAGE


UI_PAGES = [
    CUSTOMER_LIST_PAGE,
    CUSTOMER_CREATE_PAGE,
    CUSTOMER_EDIT_PAGE
]