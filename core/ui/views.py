# core/ui/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.tenants.services import TenantService
from .services import (
    UIMenuService, 
    UIPageService, 
    NavigationStrategyService,
)

from .serializers import (
    UIMenuSerializer, 
    UIPageSerializer, 
)

from .models import UIPage


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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        # ambil semua page yang user boleh akses
        pages = UIPageService.get_pages_for_user(
            user=request.user,
            tenant=tenant,
        )

        serializer = UIPageSerializer(pages, many=True)
        return Response(serializer.data)
    

class NavigationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            tenant = TenantService.get_current_tenant(request)

            nav_type = request.query_params.get("type")
            device = request.query_params.get("device", "all")

            if not nav_type:
                return Response(
                    {"detail": "type query param is required"},
                    status=400,
                )
            
            # resolve role
            role = "guest"

            if request.user.is_authenticated and request.role:
                role = request.role.code

            strategy = NavigationStrategyService.get_strategy(
                user=request.user,
                tenant=tenant,
                nav_type=nav_type,
                device=device,
                app=tenant.code,
                role=role,
            )

            if not strategy:
                return Response(
                    {"detail": "Navigation not found"},
                    status=404,
                )

            return Response(strategy)
        
        except Exception as e:
            print(e)
    
