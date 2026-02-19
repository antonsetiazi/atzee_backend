# core/ui/registry.py

from collections import defaultdict

UI_MODULE_MENUS = defaultdict(list)
UI_MODULE_PAGES = defaultdict(list)


def register_ui_module_menus(module: str, menus: list):
    UI_MODULE_MENUS[module].extend(menus)


def register_ui_module_pages(module: str, pages: list):
    # normalize supaya selalu list
    if not isinstance(pages, list):
        pages = [pages]

    UI_MODULE_PAGES[module].extend(pages)
