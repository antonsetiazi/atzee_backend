from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def core_exception_handler(exc, context):
    response = exception_handler(exc, context)

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

    response.data = {
        "error": {
            "code": getattr(exc, "default_code", "ERROR"),
            "message": response.data.get("detail", "Error"),
            "details": {},
        }
    }
    return response
