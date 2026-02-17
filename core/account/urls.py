from django.urls import path
from core.account.views import UserSettingsView

urlpatterns = [
    path("settings/", UserSettingsView.as_view(), name="user-settings"),
]
