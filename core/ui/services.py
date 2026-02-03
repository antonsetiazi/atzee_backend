# core/ui/services.py

from .models import UIMenu, UIPage
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