# verticals/apotek/api/customer_profile.py

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from business.customers.models import Customer
from verticals.apotek.models.customer_profile import ApotekCustomerProfile


# ----------------------------
# Serializer (local & simple)
# ----------------------------

class ApotekCustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApotekCustomerProfile
        fields = [
            "medical_note",
            "allergies",
            "requires_prescription",
        ]


# ----------------------------
# API View (explicit contract)
# ----------------------------

class ApotekCustomerProfileAPI(APIView):
    """
    Vertical API: Apotek Customer Profile

    GET  -> read profile
    POST -> update profile
    """

    def get_object(self, customer_id):
        customer = get_object_or_404(Customer, pk=customer_id)
        profile, _ = ApotekCustomerProfile.objects.get_or_create(
            customer=customer
        )
        return profile

    def get(self, request, customer_id):
        profile = self.get_object(customer_id)
        serializer = ApotekCustomerProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, customer_id):
        profile = self.get_object(customer_id)
        serializer = ApotekCustomerProfileSerializer(
            profile,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
