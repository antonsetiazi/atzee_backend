# accounting/api/journals/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounting.services.journal_service import JournalService
from accounting.models import Journal
from .serializers import JournalSerializer


class JournalCreateAPIView(APIView):

    def post(self, request):
        try:
            journal = JournalService.create_journal(
                tenant=request.user.tenant,
                user=request.user,
                date=request.data.get("date"),
                description=request.data.get("description", ""),
                reference=request.data.get("reference", ""),
                entries_data=request.data.get("entries", []),
                auto_post=request.data.get("auto_post", False)
            )

            return Response({
                "id": str(journal.id),
                "is_posted": journal.is_posted
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        

class JournalListAPIView(APIView):

    def get(self, request):
        tenant = request.user.tenant

        qs = Journal.objects.filter(tenant=tenant)

        # filter optional
        date_from = request.GET.get("date_from")
        date_to = request.GET.get("date_to")
        is_posted = request.GET.get("is_posted")

        if date_from:
            qs = qs.filter(date__gte=date_from)

        if date_to:
            qs = qs.filter(date__lte=date_to)

        if is_posted is not None:
            qs = qs.filter(is_posted=is_posted.lower() == "true")

        qs = qs.order_by("-date", "-created_at")[:100]

        data = JournalSerializer(qs, many=True).data

        return Response(data)        
    

class JournalDetailAPIView(APIView):

    def get(self, request, journal_id):
        try:
            journal = Journal.objects.get(
                id=journal_id,
                tenant=request.user.tenant
            )

            data = JournalSerializer(journal).data

            return Response(data)

        except Journal.DoesNotExist:
            return Response(
                {"error": "Journal not found"},
                status=status.HTTP_404_NOT_FOUND
            )    