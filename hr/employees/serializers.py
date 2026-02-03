# hr/employees/serializers.py

from rest_framework import serializers
from hr.employees.models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "employee_code",
            "full_name",
            "job_title",
            "is_active",
        ]


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "user_id",
            "employee_code",
            "full_name",
            "email",
            "phone",
            "job_title",
            "join_date",
            "is_active",
            "notes",
            "created_at",
            "updated_at",
        ]


class EmployeeCreateSerializer(serializers.Serializer):
    # user_id = serializers.UUIDField()
    employee_code = serializers.CharField(
        required=False, allow_blank=True
    )
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(
        required=False, allow_blank=True
    )
    phone = serializers.CharField(
        required=False, allow_blank=True
    )
    job_title = serializers.CharField(
        required=False, allow_blank=True
    )
    join_date = serializers.DateField()
    notes = serializers.CharField(
        required=False, allow_blank=True
    )


class EmployeeUpdateSerializer(serializers.Serializer):
    employee_code = serializers.CharField(
        required=False, allow_blank=True
    )
    full_name = serializers.CharField(required=False)
    email = serializers.EmailField(
        required=False, allow_blank=True
    )
    phone = serializers.CharField(
        required=False, allow_blank=True
    )
    job_title = serializers.CharField(
        required=False, allow_blank=True
    )
    is_active = serializers.BooleanField(required=False)
    notes = serializers.CharField(
        required=False, allow_blank=True
    )
