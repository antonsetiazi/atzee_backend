# core/permissions/registry.py

class PermissionRegistry:
    _permissions: list[dict] = []

    @classmethod
    def register(cls, permissions: list[dict]):
        cls._permissions.extend(permissions)

    @classmethod
    def all(cls):
        return cls._permissions
