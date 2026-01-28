from core.settings.models import Setting


class SettingService:

    @staticmethod
    def get_setting(key, tenant=None, default=None):
        """
        Resolve setting:
        1. Tenant-specific
        2. Global
        """
        if tenant:
            try:
                return Setting.objects.get(
                    tenant=tenant,
                    key=key
                ).value
            except Setting.DoesNotExist:
                pass

        try:
            return Setting.objects.get(
                tenant__isnull=True,
                key=key
            ).value
        except Setting.DoesNotExist:
            return default

    @staticmethod
    def get_all_settings(tenant=None):
        """
        Return merged settings:
        Tenant overrides global
        """
        result = {}

        global_settings = Setting.objects.filter(
            tenant__isnull=True
        )
        for s in global_settings:
            result[s.key] = s.value

        if tenant:
            tenant_settings = Setting.objects.filter(
                tenant=tenant
            )
            for s in tenant_settings:
                result[s.key] = s.value

        return result

    @staticmethod
    def set_setting(key, value, tenant=None):
        setting, _ = Setting.objects.update_or_create(
            tenant=tenant,
            key=key,
            defaults={"value": value}
        )
        return setting
