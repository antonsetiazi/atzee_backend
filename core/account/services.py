# core/account/services.py

from django.db import transaction
from core.account.models import UserAddress
from core.account.models import UserBankAccount
from core.master.banks.models import Bank


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


@transaction.atomic
def create_user_bank(*, tenant, user, **data):
    if data.get("is_default"):
        UserBankAccount.objects.filter(
            tenant=tenant,
            user=user
        ).update(is_default=False)

    bank = Bank.objects.filter(
        tenant=tenant,
        id=data["bank_id"],
        is_active=True,
        is_deleted=False
    ).first()

    if not bank:
        raise Exception("Bank not found")
    
    return UserBankAccount.objects.create(
        tenant=tenant,
        user=user,
        bank=bank,
        account_number=data["account_number"],
        account_name=data["account_name"],
        is_default=data.get("is_default", False),
    )


@transaction.atomic
def update_user_bank(*, tenant, user, bank_id, **data):
    bank = UserBankAccount.objects.get(
        tenant=tenant,
        user=user,
        id=bank_id
    )

    if data.get("is_default"):
        UserBankAccount.objects.filter(
            tenant=tenant,
            user=user
        ).update(is_default=False)

    for field, value in data.items():
        setattr(bank, field, value)

    bank.save()
    return bank


@transaction.atomic
def delete_user_bank(*, tenant, user, bank_id):
    bank = UserBankAccount.objects.get(
        tenant=tenant,
        user=user,
        id=bank_id
    )

    bank.is_active = False
    bank.save()


@transaction.atomic
def set_default_bank(*, tenant, user, bank_id):
    UserBankAccount.objects.filter(
        tenant=tenant,
        user=user
    ).update(is_default=False)

    bank = UserBankAccount.objects.get(
        tenant=tenant,
        user=user,
        id=bank_id
    )

    bank.is_default = True
    bank.save()

    return bank