# core/fees/utils.py

from decimal import Decimal, ROUND_HALF_UP


def to_decimal(value) -> Decimal:
    """
    Safe convert ke Decimal
    """
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def round_money(value: Decimal) -> Decimal:
    """
    Standard rounding untuk currency
    (2 decimal places)
    """
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def is_amount_in_range(
    amount: Decimal,
    min_amount: Decimal | None,
    max_amount: Decimal | None
) -> bool:
    """
    Validasi apakah amount masuk dalam range rule
    """

    if min_amount is not None and amount < min_amount:
        return False

    if max_amount is not None and amount > max_amount:
        return False

    return True


def is_category_match(
    fee_category: str | None,
    input_category: str | None
) -> bool:
    """
    Validasi kategori
    """

    if not fee_category:
        return True  # global fee

    return fee_category == input_category


def is_partner_match(
    fee_partner_id,
    input_partner_id
) -> bool:
    """
    Validasi partner-specific fee
    """

    if not fee_partner_id:
        return True

    return str(fee_partner_id) == str(input_partner_id)