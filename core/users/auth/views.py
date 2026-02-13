# core/users/auth/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .serializers import LoginSerializer, RegisterSerializer
from .services import issue_jwt_for_user

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        tenant = serializer.validated_data["tenant"]

        tokens = issue_jwt_for_user(
            user=user,
            active_tenant_id=tenant.id,
        )

        return Response({
            "user": {
                "id": str(user.id),
                "username": user.email,
                "full_name": user.full_name,
                "tenant_id": str(tenant.id),
            },
            "tokens": tokens,
        })


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.email,
            "full_name": user.full_name,
            "tenant_id": user.tenant_id
        })


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "id": str(user.id),
                "email": user.email,
                "full_name": user.full_name,
                "tenant_id": str(user.tenant_memberships.first().tenant.id),
            }, status=status.HTTP_201_CREATED)
        else:
            # Kirim error serializer ke frontend agar user tahu masalahnya
            return Response({
                "error": {
                    "message": "Validation failed",
                    "details": serializer.errors
                }
            }, status=status.HTTP_400_BAD_REQUEST)