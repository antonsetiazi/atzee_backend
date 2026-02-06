# verticals/apotek/manifest.py

from .extension.product import APOTEK_PRODUCT_EXTENSION
from .extension.customer import APOTEK_CUSTOMER_EXTENSION

VERTICAL_MANIFEST = {
    "key": "apotek",
    "name": "Apotek",
    "description": "Vertical untuk bisnis apotek dan farmasi",

    # business modules yang dipakai
    "uses": [
        "inventory",
        "products",
        "sales",
    ],

    "extensions": {
        "products": APOTEK_PRODUCT_EXTENSION,
        "customers": APOTEK_CUSTOMER_EXTENSION,
    },

    "rules": [
        "verticals.apotek.rules.validate_drug_sale",
        "verticals.apotek.rules.validate_apotek_customer",
    ],

    # permissions tambahan (belum di-hook ke logic)
    "permissions": [
        "apotek.drug.view",
        "apotek.drug.sell",
    ],

    # UI registration (nanti)
    "ui": {
        "menus": [],
        "pages": [],
    },
}
