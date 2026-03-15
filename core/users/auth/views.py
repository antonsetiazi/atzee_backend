# core/users/auth/views.py

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import (
    RegisterSerializer, 
    MeSerializer,
    ChangePasswordSerializer
)

from .serializers import RequestOTPSerializer, VerifyOTPSerializer
from .services import issue_jwt_for_user, change_user_password
from core.otp.services import OTPService
from .services import AuthService
from shared.utils.phone import normalize_phone
from core.otp.utils.hash import verify_otp

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

        try:
            user, tenant = AuthService.login_with_password(
                email=email,
                password=password,
                tenant_code=tenant_code
            )

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
                    "avatar_url": (
                        request.build_absolute_uri(user.avatar.get_download_url())
                        if user.avatar else None
                    ),
                },
                "tokens": tokens,
            })
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
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
        try:
            serializer = RequestOTPSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            phone = normalize_phone(serializer.validated_data["phone"])
            
            OTPService.send_whatsapp_otp(phone)

            return Response({
                "detail": "OTP sent"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
    

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = VerifyOTPSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            phone = normalize_phone(serializer.validated_data["phone"])
            otp = serializer.validated_data["otp"]
            tenant_code = serializer.validated_data["tenant_code"]

            try:

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

            except Exception as e:

                return Response(
                    {"detail": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                ) 
        except Exception as e:
            print(e)