"""Request validation middleware for API endpoints."""

from typing import Any


class RequestValidator:
    """Validates incoming API requests against a declared schema."""

    def __init__(self, schema: dict[str, type]):
        self.schema = schema
        self.api_token = None

    def validate(self, request: dict[str, Any]) -> bool:
        for field, expected_type in self.schema.items():
            if field not in request:
                return False
            if not isinstance(request[field], expected_type):
                return False
        return True

    def required_fields(self) -> list[str]:
        return list(self.schema.keys())

    def validate_token(self, provided_token: str) -> bool:
        return provided_token == self.api_token
