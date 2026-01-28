# core/ui/schema/serialize.py

from dataclasses import asdict
from core.ui.schema.page import Page


def page_to_dict(page: Page) -> dict:
    return asdict(page)