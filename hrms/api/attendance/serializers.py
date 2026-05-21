# hrms/api/attendance/serializers.py

from rest_framework import serializers

from hrms.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = "__all__"
