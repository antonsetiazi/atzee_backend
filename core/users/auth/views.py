# core/users/auth/views.py

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from .serializers import (
    RegisterSerializer, 
    MeSerializer,
    ChangePasswordSerializer
)

from .serializers import RequestOTPSerializer, VerifyOTPSerializer
from .services import issue_jwt_for_user, change_user_password
from .services import AuthTokenService
from .services import AuthService

from core.otp.services import OTPService
from core.otp.utils.hash import verify_otp
from shared.utils.phone import normalize_phone
from shared.api.responses import success_response
from shared.api.responses import error_response


class AuthConfigView(APIView):
    """
    Return authentication configuration used by frontend login UI.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "methods": settings.AUTH_METHODS,
            "default_method": settings.AUTH_DEFAULT_METHOD,
        })
    
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")
        tenant_code = request.data.get("tenant_code")

        user, tenant = AuthService.login_with_password(
            email=email,
            password=password,
            tenant_code=tenant_code
        )

        tokens = issue_jwt_for_user(
            user=user,
            active_tenant_id=tenant.id,
        )

        return success_response(
            data={
                "user": {
                    "id": str(user.id),
                    "username": user.email,
                    "full_name": user.full_name,
                    "tenant_id": str(tenant.id),
                    "avatar_url": (
                        request.build_absolute_uri(
                            user.avatar.get_download_url()
                        )
                        if user.avatar else None
                    ),
                },
                "tokens": tokens,
            },
            message="Login success",
        )


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = MeSerializer(
            request.user,
            context={"request": request}
        )
        return Response(serializer.data)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return success_response(
                data={
                    "id": str(user.id),
                    "email": user.email,
                    "full_name": user.full_name,
                    "tenant_id": str(
                        user.tenant_memberships.first().tenant.id
                    ),
                },
                message="Registration success",
                status_code=201,
            )
        else:
            # Kirim error serializer ke frontend agar user tahu masalahnya
            return Response({
                "error": {
                    "message": "Validation failed",
                    "details": serializer.errors
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateAvatarView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        file_id = request.data.get("file_id")

        if not file_id:
            return Response(
                {"detail": "file_id required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            file = request.user.avatar._meta.model.objects.get(id=file_id)
        except Exception:
            return Response(
                {"detail": "File not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        request.user.avatar = file
        request.user.save(update_fields=["avatar"])

        return Response({
            "avatar_url": request.build_absolute_uri(
                file.get_download_url()
            )
        })        
    

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        new_password = serializer.validated_data["new_password"]
        change_user_password(request.user, new_password)

        return Response(
            {"detail": "Password updated successfully"},
            status=status.HTTP_200_OK
        )
    

class RequestOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = normalize_phone(serializer.validated_data["phone"])
        
        OTPService.send_whatsapp_otp(phone)

        return success_response(
            message="OTP sent",
        )
    

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        phone = normalize_phone(serializer.validated_data["phone"])
        otp = serializer.validated_data["otp"]
        tenant_code = serializer.validated_data["tenant_code"]

        user, tenant = AuthService.login_with_otp(
            phone=phone,
            otp=otp,
            tenant_code=tenant_code
        )

        tokens = issue_jwt_for_user(
            user=user,
            active_tenant_id=tenant.id
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


class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"detail": "Refresh token required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)

            user_id = token.get("user_id")
            active_tenant = token.get("active_tenant")

            if not user_id or not active_tenant:
                raise InvalidToken("Invalid token payload")

            from core.users.models import User

            user = User.objects.get(id=user_id)

            tokens = AuthTokenService.issue_tokens(
                user=user,
                active_tenant_id=active_tenant
            )

            return success_response(
                data=tokens,
                message="Token refreshed",
            )

        except (TokenError, InvalidToken, User.DoesNotExist):
            return error_response(
                message="Session expired",
                code="UNAUTHORIZED",
                error_type="auth",
                status_code=401,
            )         