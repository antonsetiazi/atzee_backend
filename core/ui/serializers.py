# core/ui/serializers.py

from rest_framework import serializers
from .models import UIMenu, UIPage, TenantNavigationConfig, TenantNavigationItem


class UIMenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    permission = serializers.SerializerMethodField()

    class Meta:
        model = UIMenu
        fields = [
            "key",
            "label",
            "icon",
            "route",
            "children",
            "permission"
        ]

    def get_children(self, obj):
        children = obj.children.filter(is_active=True)
        return UIMenuSerializer(children, many=True).data

    def get_permission(self, obj):
        """
        Build standard permission code: app.resource.action
        """
        return f"{obj.app}.{obj.resource}.{obj.action}"
    

class UIPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UIPage
        fields = [
            "key",
            "title",
            "description",
            "domain",
            "entity",
            "path",
            "permissions",
            "blocks",
        ]


