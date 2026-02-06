# verticals/apotek/extensions/customer.py

from core.ui.extensions.registry import UIExtensionRegistry

APOTEK_CUSTOMER_EXTENSION = {
    "page_key": "apotek.customers.create",
    "target": "form",        # future-proof
    "mode": ["create", "edit"],
    "fields": [
        {
            "key": "medical_note",
            "type": "textarea",
            "label": "Catatan Medis",
        },
        {
            "key": "allergies",
            "type": "text",
            "label": "Alergi",
        },
        {
            "key": "requires_prescription",
            "type": "select",
            "label": "Perlu Resep",
            "options": [
                {"label": "Ya", "value": True},
                {"label": "Tidak", "value": False},
            ],
            "default": False,
        },
    ],
}

UIExtensionRegistry.register(APOTEK_CUSTOMER_EXTENSION)