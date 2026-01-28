from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import LoginSerializer
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
                "username": user.username,
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
            "username": user.username,
            "full_name": user.full_name,
            "tenant_id": user.tenant_id
        })
