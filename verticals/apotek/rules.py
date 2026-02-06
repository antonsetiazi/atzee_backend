# verticals/apotek/rules.py

from django.core.exceptions import ValidationError


def validate_apotek_customer(customer):
    if not customer.phone:
        raise ValidationError("Apotek customer must have phone number")


def validate_drug_sale(product_meta, context):
    """
    context:
        - has_prescription
        - customer_type
    """
    if not product_meta.get("is_drug"):
        return

    if product_meta.get("requires_prescription"):
        if not context.get("has_prescription"):
            raise ValueError("Obat ini memerlukan resep dokter.")
