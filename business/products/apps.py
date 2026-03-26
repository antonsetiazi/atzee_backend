from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.products"
    label = "business_products"


    def ready(self):
        from .ui import bootstrap
        import business.products.signals
        from core.entities.registry import register_entity
        from .entities.product_list import ProductListEntity
        from .entities.product_create import ProductCreateEntity

        register_entity(ProductListEntity())
        register_entity(ProductCreateEntity())