# verticals/ustadzku/seeds/categories.py

CATEGORIES = [
    {
        "code": "ceramah",
        "name": "Ceramah",
        "scope": "partners.service_category",
        "children": [
            {
                "code": "ceramah_jumat",
                "name": "Ceramah Jumat",
                "scope": "partners.service_category",
            },
            {
                "code": "ceramah_umum",
                "name": "Ceramah Umum",
                "scope": "partners.service_category",
            },
        ],
    },
    {
        "code": "akad",
        "name": "Akad Nikah",
        "scope": "partners.service_category",
    },
    {
        "code": "tahsin",
        "name": "Tahsin / Mengaji",
        "scope": "partners.service_category",
    },
]