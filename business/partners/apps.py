# business/partners/apps.py

from django.apps import AppConfig


class PartnersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.partners"
    label = "business_partners"


    def ready(self):
        from core.entities.registry import register_entity
        from .entities.partner_list import PartnerListEntity
        from .entities.partner_create import PartnerCreateEntity

        register_entity(PartnerListEntity())
        register_entity(PartnerCreateEntity())