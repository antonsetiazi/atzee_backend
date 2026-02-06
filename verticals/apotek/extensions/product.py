# verticals/apotek/extension/product.py

APOTEK_PRODUCT_EXTENSION = {
    "entity": "product",

    "fields": [
        {
            "key": "is_drug",
            "type": "boolean",
            "label": "Obat",
            "default": False,
        },
        {
            "key": "drug_type",
            "type": "choice",
            "label": "Jenis Obat",
            "choices": [
                ("otc", "Obat Bebas"),
                ("limited", "Obat Bebas Terbatas"),
                ("prescription", "Obat Resep"),
            ],
            "visible_if": {
                "is_drug": True
            }
        },
        {
            "key": "dosage_form",
            "type": "choice",
            "label": "Bentuk Sediaan",
            "choices": [
                ("tablet", "Tablet"),
                ("capsule", "Kapsul"),
                ("syrup", "Sirup"),
                ("ointment", "Salep"),
            ],
        },
        {
            "key": "strength",
            "type": "string",
            "label": "Kekuatan / Dosis",
            "example": "500 mg",
        },
        {
            "key": "requires_prescription",
            "type": "boolean",
            "label": "Perlu Resep Dokter",
            "default": False,
        },
    ]
}
