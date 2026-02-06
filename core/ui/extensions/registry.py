# core/ui/extensions/registry.py

class UIExtensionRegistry:
    _extensions: list[dict] = []

    @classmethod
    def register(cls, extension: dict):
        cls._extensions.append(extension)

    @classmethod
    def all(cls):
        return cls._extensions
