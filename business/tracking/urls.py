# business/tracking/urls.py

from django.urls import path
from business.tracking.views import UpdateLocationView, OrderTrackingView

urlpatterns = [
    path("location/", UpdateLocationView.as_view()),
    path("order/<int:order_id>/", OrderTrackingView.as_view()),
]