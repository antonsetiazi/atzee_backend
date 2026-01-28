from rest_framework import serializers
from hr.attendance.models import AttendanceRecord
from hr.attendance import services


class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = [
            "id",
            "employee_id",
            "date",
            "status",
            "check_in",
            "check_out",
        ]


class AttendanceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = [
            "id",
            "employee_id",
            "date",
            "status",
            "check_in",
            "check_out",
            "notes",
            "created_at",
            "updated_at",
        ]


class AttendanceCreateSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    date = serializers.DateField()
    status = serializers.ChoiceField(
        choices=AttendanceRecord.STATUS_CHOICES,
        required=False
    )
    check_in = serializers.DateTimeField(required=False)
    check_out = serializers.DateTimeField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        request = self.context["request"]

        return services.create_attendance(
            tenant=request.tenant,
            created_by=request.user,
            work_date=validated_data.pop("date"),
            **validated_data
        )
    

class AttendanceUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(
        choices=AttendanceRecord.STATUS_CHOICES,
        required=False
    )
    check_in = serializers.DateTimeField(required=False)
    check_out = serializers.DateTimeField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)

    def update(self, instance, validated_data):
        request = self.context["request"]

        return services.update_attendance(
            tenant=request.tenant,
            attendance_id=instance.id,
            updated_by=request.user,
            **validated_data
        )