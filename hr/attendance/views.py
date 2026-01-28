from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from hr.attendance import selectors
from hr.attendance.serializers import (
    AttendanceListSerializer,
    AttendanceDetailSerializer,
    AttendanceCreateSerializer,
    AttendanceUpdateSerializer
)


class AttendanceViewSet(viewsets.ViewSet):
    """
    Attendance API (tenant scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        qs = selectors.get_attendance_queryset(
            tenant=request.tenant
        )
        serializer = AttendanceListSerializer(
            qs, many=True
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        attendance = selectors.get_attendance_by_id(
            tenant=request.tenant,
            attendance_id=pk
        )

        if not attendance:
            return Response(
                {"detail": "Attendance not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AttendanceDetailSerializer(attendance)
        return Response(serializer.data)

    def create(self, request):
        serializer = AttendanceCreateSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        attendance = serializer.save()
        output = AttendanceDetailSerializer(attendance)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )

    def update(self, request, pk=None):
        attendance = selectors.get_attendance_by_id(
            tenant=request.tenant,
            attendance_id=pk
        )

        if not attendance:
            return Response(
                {"detail": "Attendance not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AttendanceUpdateSerializer(
            instance=attendance,
            data=request.data,
            partial=True,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        attendance = serializer.save()
        output = AttendanceDetailSerializer(attendance)

        return Response(output.data)

    def destroy(self, request, pk=None):
        from hr.attendance.services import delete_attendance

        delete_attendance(
            tenant=request.tenant,
            attendance_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
