from django.db import transaction
from core.account.models import UserAddress


@transaction.atomic
def create_user_address(*, tenant, user, **data):
    if data.get("is_default"):
        UserAddress.objects.filter(
            tenant=tenant,
            user=user
        ).update(is_default=False)

    return UserAddress.objects.create(
        tenant=tenant,
        user=user,
        **data
    )


@transaction.atomic
def update_user_address(*, tenant, user, address_id, **data):
    address = UserAddress.objects.get(
        tenant=tenant,
        user=user,
        id=address_id
    )

    if data.get("is_default"):
        UserAddress.objects.filter(
            tenant=tenant,
            user=user
        ).update(is_default=False)

    for field, value in data.items():
        setattr(address, field, value)

    address.save()
    return address


@transaction.atomic
def delete_user_address(*, tenant, user, address_id):
    address = UserAddress.objects.get(
        tenant=tenant,
        user=user,
        id=address_id
    )

    address.is_active = False
    address.save()


@transaction.atomic
def set_default_address(*, tenant, user, address_id):
    UserAddress.objects.filter(
        tenant=tenant,
        user=user
    ).update(is_default=False)

    address = UserAddress.objects.get(
        tenant=tenant,
        user=user,
        id=address_id
    )

    address.is_default = True
    address.save()

    return address