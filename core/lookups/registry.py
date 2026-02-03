# core/lookups/registry.py

from typing import Callable

_LOOKUPS: dict[str, Callable[[], list[dict]]] = {}


def register_lookup(key: str, provider: Callable[[], list[dict]]):
    _LOOKUPS[key] = provider


def get_lookup(key: str):
    return _LOOKUPS.get(key)
