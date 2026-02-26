# core/users/auth/urls.py

from django.urls import path
from .views import (
    LoginView, 
    MeView, 
    RegisterView, 
    UpdateAvatarView,
    ChangePasswordView
)

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("me/", MeView.as_view()),
    path("register/", RegisterView.as_view()),
    path("me/avatar/", UpdateAvatarView.as_view()),
    path("change-password/", ChangePasswordView.as_view()), 
]
