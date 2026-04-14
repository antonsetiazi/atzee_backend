# business/reviews/apps.py

from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.reviews"
    label = "business_reviews"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.review_list import ReviewListEntity

        register_entity(ReviewListEntity())