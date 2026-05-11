# accounting/api/asset_categories/selectors.py

from accounting.models import AssetCategory


def get_asset_categories(*, tenant, search=None):

    qs = AssetCategory.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )

    if search:
        qs = qs.filter(name__icontains=search)

    return qs.order_by("code")


def get_asset_category_by_id(*, tenant, asset_category_id):

    return AssetCategory.objects.get(
        tenant=tenant,
        id=asset_category_id,
        is_deleted=False,
    )
