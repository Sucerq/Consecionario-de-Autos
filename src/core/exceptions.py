from fastapi import status
from datetime import datetime
from typing import Any


class AppException(Exception):

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        code: str | None = None,
        details: dict | list | None = None,
    ):
        self.message = message
        self.status_code = status_code
        self.code = code or "ERROR"
        self.details = details
        self.timestamp = datetime.utcnow()
        super().__init__(message)


class NotFoundError(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    code = "NOT_FOUND"

    def __init__(
        self, message: str = "Recurso no encontrado", details: dict | list | None = None
    ):
        super().__init__(
            message,
            self.status_code,
            self.code,
            details,
        )


class ConflictError(AppException):
    status_code = status.HTTP_409_CONFLICT
    code = "CONFLICT"

    def __init__(
        self,
        message: str,
        details: dict | list | None = None,
    ):
        super().__init__(message, self.status_code, self.code, details)


class BadRequestError(AppException):

    status_code = status.HTTP_400_BAD_REQUEST
    code = "BAD_REQUEST"

    def __init__(self, message: str, details: dict | list | None = None):
        super().__init__(
            message,
            self.status_code,
            self.code,
            details=details,
        )


class ValidationError(AppException):
    """Error de validación de datos (422)."""

    def __init__(self, message: str, details: dict | list | None = None):
        super().__init__(
            message=message,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            code="VALIDATION_ERROR",
            details=details,
        )


class UnauthorizedError(AppException):

    status_code = status.HTTP_401_UNAUTHORIZED
    code = "UNAUTHORIZED"

    def __init__(
        self,
        message: str = "No autenticado",
        details: dict[str, Any] | list[Any] | None = None,
    ):
        super().__init__(message, self.status_code, self.code, details)


class ForbiddenError(AppException):

    status_code = status.HTTP_403_FORBIDDEN
    code = "FORBIDDEN"

    def __init__(
        self,
        message: str = "No tienes permisos para esta acción",
        details: dict[str, Any] | list[Any] | None = None,
    ):
        super().__init__(message, self.status_code, self.code, details)
