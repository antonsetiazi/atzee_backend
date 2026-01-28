from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.settings.services import SettingService
from core.permissions.decorators import permission_required


class SettingListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = getattr(request, "tenant", None)
        data = SettingService.get_all_settings(tenant=tenant)
        return Response(data)

    @permission_required("core.settings", "setting", "update")
    def put(self, request):
        tenant = getattr(request, "tenant", None)

        for key, value in request.data.items():
            SettingService.set_setting(
                key=key,
                value=value,
                tenant=tenant
            )

        return Response({"status": "updated"})
