# hrms/api/payroll/serializers.py

from rest_framework import serializers

from hrms.models import Payroll


class PayrollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payroll
        fields = "__all__"
