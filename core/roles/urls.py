from django.urls import path
from core.roles.views import RoleListCreateView, RoleDetailView

urlpatterns = [
    path("", RoleListCreateView.as_view()),
    path("<uuid:role_id>/", RoleDetailView.as_view()),
]
