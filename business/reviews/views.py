# business/reviews/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from core.tenants.services import TenantService
from .serializers import (
    CreateReviewSerializer,
    ReviewOutputSerializer
)
from .services import create_review
from .models import Review


class CreateReviewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            tenant = TenantService.get_current_tenant(request)

            serializer = CreateReviewSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            review = create_review(
                tenant=tenant,
                user=request.user,
                booking_id=serializer.validated_data["booking_id"],
                rating=serializer.validated_data["rating"],
                comment=serializer.validated_data.get("comment", ""),
            )

            return Response(
                ReviewOutputSerializer(review).data,
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class PartnerReviewListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, partner_id):
        tenant = TenantService.get_current_tenant(request)

        reviews = Review.objects.filter(
            tenant=tenant,
            partner_id=partner_id
        ).select_related("user")

        data = ReviewOutputSerializer(reviews, many=True).data
        return Response(data)
    

class BookingReviewDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, booking_id):
        tenant = TenantService.get_current_tenant(request)

        review = Review.objects.filter(
            tenant=tenant,
            booking_id=booking_id,
            user=request.user
        ).select_related("user").first()

        if not review:
            return Response(None, status=200)

        data = ReviewOutputSerializer(review).data
        return Response(data)    