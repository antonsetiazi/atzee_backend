from django.apps import AppConfig
# from core.permissions.registry import PermissionRegistry
# from .permissions import PERMISSIONS

class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.products"
    label = "business_product"

    # def ready(self):
        # PermissionRegistry.register(PERMISSIONS)

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.product_list import ProductListEntity
        from .entities.product_create import ProductCreateEntity

        register_entity(ProductListEntity())
        register_entity(ProductCreateEntity())