# core/lookups/services.py

from .registry import get_lookup


class LookupService:
    @staticmethod
    def execute(key: str) -> list[dict]:
        provider = get_lookup(key)

        if not provider:
            raise ValueError("Lookup not found")

        return provider()
