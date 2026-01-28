# core/ui/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from .services import UIMenuService, UIPageService
from .serializers import UIMenuSerializer, UIPageSerializer

class UIMenuView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        menus = UIMenuService.get_menu_for_user(
            user=request.user,
            tenant=tenant,
        )
        # print("menus: ", menus)
        serializer = UIMenuSerializer(menus, many=True)
        return Response(serializer.data)


class UIPageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, page_key):
        tenant = TenantService.get_current_tenant(request)

        page = UIPageService.get_page_for_user(
            user=request.user,
            tenant=tenant,
            page_key=page_key,
        )

        if not page:
            return Response(
                {"detail": "Page not found"},
                status=404,
            )

        serializer = UIPageSerializer(page)
        return Response(serializer.data)


class UIPageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        # ambil semua page yang user boleh akses
        pages = UIPageService.get_pages_for_user(
            user=request.user,
            tenant=tenant,
        )

        serializer = UIPageSerializer(pages, many=True)
        return Response(serializer.data)