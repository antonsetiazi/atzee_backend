# shared/ui/bootstrap.py

from core.ui.models import UIMenu, UIPage
from core.ui.schema.page import Page
from core.ui.schema.menu import Menu 
from core.ui.schema.serialize import page_to_dict
from core.ui.extensions.registry import UIExtensionRegistry


def load_ui_extensions():
    import verticals.apotek.extensions.customer


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

        # print(page_data.get('key'))
        # print(page_data)
        # print(page_data.get('description'))
        
        if not isinstance(page_data, dict):
            raise ValueError(f"Invalid page schema: {page_data}")

        # 🔒 DOMAIN WAJIB
        if "domain" not in page_data or not page_data["domain"]:
            raise ValueError(
                f"UIPage '{page_data.get('key')}' missing required field: domain"
            )

        # 🔒 ENTITY WAJIB
        if "entity" not in page_data or not page_data["entity"]:
            raise ValueError(
                f"UIPage '{page_data.get('key')}' missing required field: entity"
            )

        # pastikan blocks selalu ada
        if "blocks" not in page_data:
            columns = page_data.pop("columns", [])
            page_data["blocks"] = (
                [{"type": "table", "columns": columns}] if columns else []
            )

        # apply_ui_extensions(page_data)

        # permissions optional tapi konsisten
        page_data.setdefault("permissions", [])

        page_model.objects.update_or_create(
            key=page_data["key"],
            defaults={
                "title": page_data["title"],
                "description": page_data.get('description'),
                "domain": page_data["domain"],   # 🔥 FIX UTAMA
                "entity": page_data["entity"],
                "path": page_data.get("path"),
                "permissions": page_data["permissions"],
                "blocks": page_data["blocks"],
                "data_source": page_data["data_source"],
                "method": page_data["method"],
                "accept_context": page_data.get("accept_context", True),
                "payload_from_context": page_data.get("payload_from_context", True),
                "is_active": page_data.get("is_active", True),
                "meta": page_data.get("meta") or {},
            },
        )


def seed_ui(*, menus: list[dict] = None, pages: list[dict] = None,
            menu_model=UIMenu, page_model=UIPage):
    """
    Seeder all-in-one: menus + pages
    """
    if menus:
        seed_menus(menus, menu_model=menu_model)
    if pages:
        # load_ui_extensions()
        seed_pages(pages, page_model=page_model)


def apply_ui_extensions(page_data: dict):
    # print("apply_ui_extensions")
    page_key = page_data.get("key")
    blocks = page_data.get("blocks", [])
    # print("UIExtensionRegistry.all():", UIExtensionRegistry.all())
    for ext in UIExtensionRegistry.all():
        if ext.get("page_key") != page_key:
            continue

        for block in blocks:
            if block.get("type") != ext.get("block", "form"):
                continue

            if "mode" in ext and block.get("mode") not in ext["mode"]:
                continue

            fields = block.setdefault("fields", [])
            existing_keys = {f["key"] for f in fields if "key" in f}

            for field in ext.get("fields", []):
                if field["key"] not in existing_keys:
                    fields.append(field)


