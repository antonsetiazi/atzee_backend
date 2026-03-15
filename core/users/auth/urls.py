# core/users/auth/urls.py

from django.urls import path
from .views import (
    AuthConfigView,
    LoginView, 
    MeView, 
    RegisterView, 
    UpdateAvatarView,
    ChangePasswordView
)

from .views import RequestOTPView, VerifyOTPView

urlpatterns = [
    path("config/", AuthConfigView.as_view()),
    
    path("login/", LoginView.as_view()),
    path("me/", MeView.as_view()),
    path("register/", RegisterView.as_view()),
    path("me/avatar/", UpdateAvatarView.as_view()),
    path("change-password/", ChangePasswordView.as_view()), 

    # OTP AUTH
    path("request-otp/", RequestOTPView.as_view()),
    path("verify-otp/", VerifyOTPView.as_view()),
]
