# core/notifications/views.py

from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from core.notifications.models import Notification
from core.notifications.serializers import NotificationSerializer

from core.tenants.services import TenantService

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        qs = Notification.objects.filter(
            user=request.user,
            tenant=tenant
        )

        # Optional filters
        is_read = request.query_params.get("is_read")
        event = request.query_params.get("event")

        if is_read is not None:
            qs = qs.filter(is_read=is_read.lower() == "true")

        if event:
            qs = qs.filter(event=event)

        serializer = NotificationSerializer(qs, many=True)
        return Response(serializer.data)


class NotificationUnreadCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = Notification.objects.filter(
            user=request.user,
            tenant=getattr(request, "tenant", None),
            is_read=False
        ).count()

        return Response({"unread_count": count})
    

class NotificationMarkReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            notif = Notification.objects.get(
                pk=pk,
                user=request.user
            )
        except Notification.DoesNotExist:
            return Response(
                {"detail": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        notif.is_read = True
        notif.save(update_fields=["is_read"])

        return Response({"status": "ok"})


class NotificationMarkAllReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Notification.objects.filter(
            user=request.user,
            tenant=getattr(request, "tenant", None),
            is_read=False
        ).update(is_read=True)

        return Response({"status": "ok"})
