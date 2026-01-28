# shared/ui/bootstrap.py

from core.ui.models import UIMenu, UIPage
from core.ui.schema.page import Page
from core.ui.schema.menu import Menu 
from core.ui.schema.serialize import page_to_dict


def seed_menus(menus: list, menu_model=UIMenu):
    """
    Generic UI menu seeder. Idempotent.
    Accepts dict OR Menu schema.
    """
    menu_map = {menu.key: menu for menu in menu_model.objects.all()}

    for item in menus:
        # 🔹 BRIDGE: typed Menu -> dict
        if isinstance(item, Menu):
            data = item.to_dict()
        else:
            data = item

        if not isinstance(data, dict):
            raise ValueError(f"Invalid menu schema: {data}")

        parent = menu_map.get(data["parent"]) if data.get("parent") else None

        menu, _ = menu_model.objects.update_or_create(
            key=data["key"],
            defaults={
                "label": data["label"],
                "icon": data.get("icon"),
                "parent": parent,
                "app": data["app"],
                "resource": data["resource"],
                "action": data["action"],
                "route": data["route"],
                "order": data.get("order", 0),
                "is_active": data.get("is_active", True),
            }
        )
        menu_map[menu.key] = menu


def seed_pages(pages: list[dict], page_model=UIPage):
    """
    Generic UI page seeder. Idempotent.
    Kolom/table disimpan langsung di field JSON (blocks)
    """
    for page_data in pages:

        # 🔹 BRIDGE: typed Page -> dict
        if isinstance(page_data, Page):
            page_data = page_to_dict(page_data)
            
        # jika sudah ada blocks, gunakan, kalau tidak buat dari columns
        if "blocks" not in page_data:
            columns = page_data.pop("columns", [])
            page_data["blocks"] = [{"type": "table", "columns": columns}] if columns else []

        # pastikan entity selalu ada
        page_data.setdefault("entity", page_data["key"].split(".")[0])

        # pastikan permissions ada
        page_data.setdefault("permissions", [])

        page_model.objects.update_or_create(
            key=page_data["key"],
            defaults=page_data,
        )


def seed_ui(*, menus: list[dict] = None, pages: list[dict] = None,
            menu_model=UIMenu, page_model=UIPage):
    """
    Seeder all-in-one: menus + pages
    """
    if menus:
        seed_menus(menus, menu_model=menu_model)
    if pages:
        seed_pages(pages, page_model=page_model)
