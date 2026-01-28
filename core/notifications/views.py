from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.notifications.models import Notification
from core.notifications.serializers import NotificationSerializer


class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Notification.objects.filter(
            user=request.user,
            tenant=getattr(request, "tenant", None)
        )

        serializer = NotificationSerializer(qs, many=True)
        return Response(serializer.data)


class NotificationMarkReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        notif = Notification.objects.get(
            pk=pk,
            user=request.user
        )
        notif.is_read = True
        notif.save(update_fields=["is_read"])

        return Response({"status": "ok"})
