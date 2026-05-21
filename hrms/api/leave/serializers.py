# hrms/api/leave/serializers.py

from rest_framework import serializers

from hrms.models import LeaveRequest


class LeaveRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaveRequest
        fields = "__all__"
