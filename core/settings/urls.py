from django.urls import path
from core.settings.views import SettingListView

urlpatterns = [
    path("", SettingListView.as_view(), name="settings"),
]
