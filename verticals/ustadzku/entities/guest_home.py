# verticals/ustadzku/entities/guest_home.py

from django.utils import timezone
from django.db import models

from core.entities.contracts import BaseEntity
from core.widgets import selectors
from verticals.ustadzku.enum.permissions import UstadzkuPermission


class GuestHomeEntity(BaseEntity):
    """
    ustadzku.guest.home entity
    """

    key = "guest.home"
    domain = "ustadzku"
    permission = UstadzkuPermission.GUEST_HOME_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        now = timezone.now()

        try:
            # -----------------------------------------
            # BANNERS (FROM UIWidget)
            # -----------------------------------------
            widgets = selectors.get_active_widgets_for_user(
                tenant=tenant,
                user=user,
            )

            banners = []

            for w in widgets:
                if w.type != "banner":
                    continue

                config = w.config or {}

                if isinstance(config, list):
                    config = config[0] if config else {}

                banners.append({
                    "id": str(w.id),
                    "title": w.title,
                    "image_url": config.get("image_url"),
                    "link_url": config.get("link_url"),
                    "open_in_new_tab": config.get("open_in_new_tab", True),
                })

            # -----------------------------------------
            # FINAL RESPONSE (FLAT STRUCTURE)
            # -----------------------------------------
            return {
                "banners": banners,
            }

        except Exception as e:
            print(e)
            return {
                "banners": None,
            }