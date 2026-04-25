# shared/api/responses.py

from rest_framework.response import Response


def success_response(
    data=None,
    message="Success",
    meta=None,
    status_code=200,
):
    return Response(
        {
            "data": data,
            "message": message,
            "meta": meta,
        },
        status=status_code,
    )


def error_response(
    *,
    message,
    code="ERROR",
    error_type="business",
    details=None,
    status_code=400,
):
    return Response(
        {
            "error": {
                "code": code,
                "message": message,
                "type": error_type,
                "details": details,
            }
        },
        status=status_code,
    )