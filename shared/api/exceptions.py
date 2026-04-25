# shared/api/exceptions.py

class BusinessException(Exception):
    def __init__(
        self,
        message="Business error",
        code="BUSINESS_ERROR",
        details=None,
        status_code=400,
    ):
        self.message = message
        self.code = code
        self.details = details
        self.status_code = status_code
        super().__init__(message)