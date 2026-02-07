# core/events/bus.py

from collections import defaultdict
from typing import Callable, Dict, List

_EVENT_REGISTRY: Dict[str, List[Callable]] = defaultdict(list)


def register_event_listener(event_name: str, handler: Callable):
    _EVENT_REGISTRY[event_name].append(handler)


def emit_event(*, name: str, payload: dict):
    """
    Emit synchronous event.
    """
    for handler in _EVENT_REGISTRY.get(name, []):
        handler(payload)
