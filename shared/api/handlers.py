# shared/api/handlers.py

from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from shared.api.exceptions import BusinessException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, BusinessException):
        return Response(
            {
                "error": {
                    "code": exc.code,
                    "message": exc.message,
                    "type": "business",
                    "details": exc.details,
                }
            },
            status=exc.status_code,
        )

    if response is None:
        return Response(
            {
                "error": {
                    "code": "SERVER_ERROR",
                    "message": "Internal server error",
                    "type": "server",
                    "details": None,
                }
            },
            status=500,
        )

    status_code = response.status_code
    data = response.data

    # Validation Error
    if isinstance(exc, ValidationError):
        return Response(
            {
                "error": {
                    "code": "VALIDATION_ERROR",
                    "message": "Validation failed",
                    "type": "validation",
                    "details": data,
                }
            },
            status=status_code,
        )

    # 401
    if status_code == 401:
        return Response(
            {
                "error": {
                    "code": "UNAUTHORIZED",
                    "message": "Authentication required",
                    "type": "auth",
                    "details": None,
                }
            },
            status=401,
        )

    # 403
    if status_code == 403:
        return Response(
            {
                "error": {
                    "code": "FORBIDDEN",
                    "message": "Access denied",
                    "type": "auth",
                    "details": None,
                }
            },
            status=403,
        )

    # 404
    if status_code == 404:
        return Response(
            {
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Data not found",
                    "type": "business",
                    "details": None,
                }
            },
            status=404,
        )

    # fallback
    return Response(
        {
            "error": {
                "code": "REQUEST_ERROR",
                "message": "Request failed",
                "type": "business",
                "details": data,
            }
        },
        status=status_code,
    )