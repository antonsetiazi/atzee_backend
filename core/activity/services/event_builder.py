# core/activity/services/event_builder.py

from typing import Any, Dict


class EventBuilder:
    """
    Utility helper for building structured event metadata.

    Used to standardize:
    - before/after diffs
    - change logs
    - audit payloads
    - workflow metadata
    """

    @staticmethod
    def build_changes(
        before: dict,
        after: dict,
    ) -> Dict[str, Any]:
        """
        Generate field-level diff structure.

        Example:
        {
            "status": {
                "before": "draft",
                "after": "approved"
            }
        }
        """

        changes = {}

        all_keys = set(before.keys()) | set(after.keys())

        for key in all_keys:
            before_value = before.get(key)
            after_value = after.get(key)

            if before_value != after_value:
                changes[key] = {
                    "before": before_value,
                    "after": after_value,
                }

        return changes

    @staticmethod
    def build_metadata(
        *,
        changes: dict = None,
        tags: list = None,
        extra: dict = None,
    ) -> Dict[str, Any]:
        """
        Standardized metadata structure.
        """

        return {
            "changes": changes or {},
            "tags": tags or [],
            "extra": extra or {},
        }
