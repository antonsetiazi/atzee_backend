# core/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="core.master",
        label="Master",
        app="core",
        resource="core",
        action="view",
        route="/core",
        order=10,
    ),
    Menu(
        key="core.org",
        label="Organization",
        app="core",
        resource="core",
        action="view",
        route="/core",
        order=20,
    ),
    Menu(
        key="core.geo",
        label="Geo",
        app="core",
        resource="core",
        action="view",
        route="/core",
        order=30,
    ),
    Menu(
        key="core.classifications",
        label="Classification",
        app="core",
        resource="core",
        action="view",
        route="/core",
        order=40,
    ),
    Menu(
        key="core.schedule",
        label="Schedule",
        app="core",
        resource="core",
        action="view",
        route="/core/schedule",
        order=50,
    ),

    # =====================
    # USER MANAGEMENT
    # =====================
    Menu(
        key="users",
        label="Users & Access",
        app="core",
        resource="users",
        action="view",
        route="/users",
        order=90,
    ),
    Menu(
        key="users.list",
        label="Users",
        parent="users",
        app="core",
        resource="users",
        action="view",
        route="/users",
        order=91,
    ),
    Menu(
        key="roles.list",
        label="Roles",
        parent="users",
        app="core",
        resource="roles",
        action="view",
        route="/roles",
        order=92,
    ),
    Menu(
        key="permissions.list",
        label="Permissions",
        parent="users",
        app="core",
        resource="permissions",
        action="view",
        route="/permissions",
        order=93,
    ),

    # =====================
    # SYSTEM
    # =====================
    Menu(
        key="system",
        label="System",
        app="core",
        resource="core",
        action="view",
        route="/system",
        order=100,
    ),
    Menu(
        key="tenants.list",
        label="Tenants",
        parent="system",
        icon="building",
        app="core",
        resource="tenants",
        action="view",
        route="/tenants",
        order=101,
    ),
    Menu(
        key="audit_logs.list",
        label="Audit Logs",
        parent="system",
        app="core",
        resource="audit_logs",
        action="view",
        route="/audit-logs",
        order=102,
    ),
    Menu(
        key="settings.general",
        label="Settings",
        parent="system",
        app="core",
        resource="settings",
        action="view",
        route="/settings",
        order=103,
    ),
]

register_ui_module_menus("core", UI_MENUS)