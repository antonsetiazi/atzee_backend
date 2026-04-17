# business/partners/apps.py

from django.apps import AppConfig


class PartnersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.partners"
    label = "business_partners"


    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.partner_list import PartnerListEntity
        from .entities.partner_create import PartnerCreateEntity
        from .entities.partner_search import PartnerSearchEntity
        from .entities.partner_detail import PartnerDetailEntity
        from .entities.partner_me import PartnerMeEntity
        from .entities.partner_me_update import PartnerMeUpdateEntity

        register_entity(PartnerListEntity())
        register_entity(PartnerCreateEntity())
        register_entity(PartnerSearchEntity())
        register_entity(PartnerDetailEntity())
        register_entity(PartnerMeEntity())
        register_entity(PartnerMeUpdateEntity())