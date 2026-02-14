# core/widgets/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="widgets",
        parent="",
        label="Widgets",
        icon="widgets",
        app="core",
        resource="widgets",
        action="view",
        route="/settings/widgets",
        order=40,
    ),
    Menu(
        key="widgets.banners.list",
        parent="widgets",
        label="Banner",
        icon="widgets",
        app="core",
        resource="widgets",
        action="view",
        route="/widgets/banners",
        order=10,
    ),
    Menu(
        key="widgets.videos.list",
        parent="widgets",
        label="Video",
        icon="widgets",
        app="core",
        resource="widgets",
        action="view",
        route="/widgets/videos",
        order=20,
    ),
]
