# core/account/services.py

from django.db import transaction
from core.account.models import UserAddress
from core.account.models import UserBankAccount
from core.master.banks.models import Bank
from core.geo.countries.models import Country
from core.geo.regions.models import Region
from core.geo.cities.models import City
from rest_framework.exceptions import ValidationError


def resolve_geo_refs(data):
    country = None
    region = None
    city = None

    country_id = data.pop("country_ref_id", None)
    region_id = data.pop("region_ref_id", None)
    city_id = data.pop("city_ref_id", None)

    if country_id:
        country = Country.objects.filter(id=country_id).first()
        if not country:
            raise ValidationError("Country not found.")

    if region_id:
        region = Region.objects.filter(id=region_id).first()
        if not region:
            raise ValidationError("Region not found.")

    if city_id:
        city = City.objects.filter(id=city_id).first()
        if not city:
            raise ValidationError("City not found.")

    # Validasi relasi city-region-country
    if city and region and city.region_id != region.id:
        raise ValidationError("City does not belong to selected region.")

    if region and country and region.country_id != country.id:
        raise ValidationError("Region does not belong to selected country.")

    return country, region, city


@transaction.atomic
def create_user_address(*, tenant, user, **data):
    if data.get("is_default"):
        UserAddress.objects.filter(
            tenant=tenant,
            user=user
        ).update(is_default=False)

    country, region, city = resolve_geo_refs(data)

    return UserAddress.objects.create(
        tenant=tenant,
        user=user,

        country_ref=country,
        region_ref=region,
        city_ref=city,

        # legacy text
        country=country.name if country else data.get("country", ""),
        region=region.name if region else data.get("region", ""),
        city=city.name if city else data.get("city", ""),

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

    country, region, city = resolve_geo_refs(data)

    for field, value in data.items():
        setattr(address, field, value)

    if country:
        address.country_ref = country
        address.country = country.name

    if region:
        address.region_ref = region
        address.region = region.name

    if city:
        address.city_ref = city
        address.city = city.name

    address.save()
    return address


@transaction.atomic
def delete_user_address(*, tenant, user, address_id):
    address = UserAddress.objects.get(
        tenant=tenant,
        user=user,
        id=address_id
    )

    address.delete()


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