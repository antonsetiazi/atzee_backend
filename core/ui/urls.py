# core/ui/urls.py

from django.urls import path
from .views import UIMenuView, UIPageView, UIPageListView

urlpatterns = [
    path("menu", UIMenuView.as_view(), name="ui-menu"),
    path("pages/<str:page_key>/", UIPageView.as_view()),
    path("pages/", UIPageListView.as_view(), name="ui-page-list"),
]
