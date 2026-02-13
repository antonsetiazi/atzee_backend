# core/ui/services.py

from typing import Dict, Any, Optional
from .models import (
    UIMenu, 
    UIPage, 
    TenantNavigationConfig, 
    TenantNavigationItem
)
from core.permissions.services import PermissionService


class UIMenuService:

    @staticmethod
    def get_menu_for_user(user, tenant):
        """
        Build menu tree based on permission engine
        """
        # permission_service = PermissionService(user=user, tenant=tenant)

        allowed_menu_keys = []

        for menu in UIMenu.objects.filter(is_active=True):
            permission_code = f"{menu.app}.{menu.resource}.{menu.action}"

            if PermissionService.can_access(
                user=user,
                tenant=tenant,
                permission_code=permission_code,
            ):
                allowed_menu_keys.append(menu.key)

        menus = (
            UIMenu.objects
            .filter(key__in=allowed_menu_keys, parent__isnull=True)
            .order_by("order")
        )

        return menus


class UIPageService:

    @staticmethod
    def get_page_for_user(user, tenant, page_key):
        try:
            page = UIPage.objects.get(
                key=page_key,
                is_active=True,
            )

        except UIPage.DoesNotExist:
            return None

        # page-level permission (declarative)
        for permission_code in page.permissions:
            if not PermissionService.can_access(
                user=user,
                tenant=tenant,
                permission_code=permission_code,
            ):
                return None
            
        return page


    @staticmethod
    def get_pages_for_user(user, tenant):
        """
        Ambil semua page yang aktif dan user boleh akses (permission)
        """
        pages = UIPage.objects.filter(is_active=True).order_by("key")
        allowed_pages = []

        from core.permissions.services import PermissionService

        for page in pages:
            # cek page-level permission
            allowed = True
            for perm_code in page.permissions:
                if not PermissionService.can_access(user=user, tenant=tenant, permission_code=perm_code):
                    allowed = False
                    break
            if allowed:
                allowed_pages.append(page)

        return allowed_pages
    

class TenantNavigationService:

    @staticmethod
    def get_navigation_for_user(user, tenant, nav_type=None, app=None, role=None):
        """
        Ambil navigation config yang aktif untuk tenant, user role, app, dan tipe (bottom/sidebar)
        """
        qs = TenantNavigationConfig.objects.filter(
            tenant=tenant,
            is_active=True,
        )

        if nav_type:
            qs = qs.filter(type=nav_type)
        if app:
            qs = qs.filter(app=app)
        if role:
            qs = qs.filter(role=role)

        # ambil pertama kalau ada lebih dari 1
        config = qs.first()
        return config    
    

class NavigationStrategyService:

    @staticmethod
    def get_strategy(
        *,
        user,
        tenant,
        nav_type: str,
        device: str = "all",
        app: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Return resolved navigation strategy ready for frontend.
        """

        queryset = TenantNavigationConfig.objects.filter(
            tenant=tenant,
            type=nav_type,
            device=device,
            is_active=True,
        )

        if app:
            queryset = queryset.filter(app=app)

        if role:
            queryset = queryset.filter(role=role)

        config = queryset.first()

        if not config:
            return None

        items_data = []

        items = config.items.filter(is_active=True).order_by("order")

        for item in items:
            resolved = NavigationStrategyService._resolve_item(
                user=user,
                tenant=tenant,
                item=item,
            )

            if resolved:
                items_data.append(resolved)

        return {
            "type": config.type,
            "device": config.device,
            "app": config.app,
            "items": items_data,
        }

    # ----------------------------------------
    # PRIVATE RESOLUTION ENGINE
    # ----------------------------------------

    @staticmethod
    def _resolve_item(*, user, tenant, item: TenantNavigationItem):

        # 1️⃣ Permission Check (if menu-based)
        if item.action_type == "menu" and item.menu:
            permission_code = f"{item.menu.app}.{item.menu.resource}.{item.menu.action}"

            if not PermissionService.can_access(
                user=user,
                tenant=tenant,
                permission_code=permission_code,
            ):
                return None

        # 2️⃣ Resolve Label
        label = None

        # Priority 1: override
        if item.label_override:
            label = item.label_override

        # Priority 2: menu label
        elif item.action_type == "menu" and item.menu:
            label = item.menu.label

        # Priority 3: page title (NEW)
        elif item.action_type == "page":
            try:
                page = UIPage.objects.get(
                    key=item.target,
                    is_active=True,
                )
                label = page.title
            except UIPage.DoesNotExist:
                label = item.target

        # Fallback
        else:
            label = item.target

        # 3️⃣ Resolve Icon
        icon = (
            item.icon_override
            or (item.menu.icon if item.menu else None)
        )

        # 4️⃣ Resolve Route
        route = (
            item.route_override
            or (item.menu.route if item.menu else None)
            or NavigationStrategyService._resolve_route_from_target(item)
        )

        # 5️⃣ Resolve Badge (placeholder for now)
        badge = None
        if item.badge_source:
            badge = NavigationStrategyService._resolve_badge(
                user=user,
                tenant=tenant,
                badge_source=item.badge_source,
            )

        return {
            "label": label,
            "icon": icon,
            "action_type": item.action_type,
            "target": item.target,
            "route": route,
            "is_primary": item.is_primary,
            "badge": badge,
        }

    @staticmethod
    def _resolve_route_from_target(item: TenantNavigationItem):

        if item.action_type == "page":
            try:
                page = UIPage.objects.get(key=item.target, is_active=True)
                return page.path
            except UIPage.DoesNotExist:
                return None

        # entity/workflow/custom handled by frontend router
        return None

    @staticmethod
    def _resolve_badge(*, user, tenant, badge_source: str):
        """
        Placeholder badge engine.
        Later we can map this to service registry.
        """
        return None    