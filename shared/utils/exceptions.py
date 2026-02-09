# shared/utils/exceptions.py

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


def core_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Unexpected error (500)
    if response is None:
        return Response(
            {
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": "Internal server error",
                    "details": {},
                }
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    message = "Error"
    details = {}

    # 🔑 HANDLE VALIDATION ERROR PROPERLY
    if isinstance(exc, ValidationError):
        data = response.data

        # Case 1: ValidationError("msg") → list
        if isinstance(data, list):
            message = data[0]

        # Case 2: ValidationError({"field": ["msg"]})
        elif isinstance(data, dict):
            if "non_field_errors" in data:
                message = data["non_field_errors"][0]
            else:
                message = "Validation error"
            details = data

    # Other DRF errors (PermissionDenied, NotAuthenticated, etc)
    else:
        if isinstance(response.data, dict):
            message = response.data.get("detail", "Error")

    response.data = {
        "error": {
            "code": getattr(exc, "default_code", "ERROR"),
            "message": message,
            "details": details,
        }
    }
    return response
