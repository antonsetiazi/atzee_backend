# verticals/finance/seeds/partners.py

PARTNERS = [
    {
        "code": "SUPP-001",
        "name": "PT Sinar Niaga Abadi",
        "email": "procurement@sinarga.co.id",
        "phone": "021-550-1200",
        "country_code": "ID",
        "region_code": "31",
        "city_code": "31.71",
        "address": "Jl. Jend. Sudirman No. 88, Jakarta Pusat",
        "latitude": -6.2088,
        "longitude": 106.8456,
        "base_price": 0,
        "rating_avg": 4.9,
        "rating_count": 128,
        "notes": (
            "Strategic supplier for office supplies, "
            "corporate inventory, and operational procurement."
        ),
        "products": [
            {
                "code": "OFFICE-001",
                "name": "Office Operational Supplies",
                "category_code": "office",
                "price": 2500000,
                "duration_minutes": 0,
            },
            {
                "code": "IT-001",
                "name": "IT Equipment Procurement",
                "category_code": "it",
                "price": 15000000,
                "duration_minutes": 0,
            },
        ],
    },
    {
        "code": "SUPP-002",
        "name": "PT Global Teknologi Nusantara",
        "email": "finance@globaltek.id",
        "phone": "021-7788-9900",
        "country_code": "ID",
        "region_code": "32",
        "city_code": "32.75",
        "address": "Jl. Asia Afrika No. 120, Bandung",
        "latitude": -6.9175,
        "longitude": 107.6191,
        "base_price": 0,
        "rating_avg": 4.8,
        "rating_count": 92,
        "notes": (
            "Enterprise technology vendor for servers, "
            "network devices, and cloud infrastructure."
        ),
        "products": [
            {
                "code": "SERVER-001",
                "name": "Dedicated Server Infrastructure",
                "category_code": "infrastructure",
                "price": 85000000,
                "duration_minutes": 0,
            },
            {
                "code": "NETWORK-001",
                "name": "Enterprise Network Equipment",
                "category_code": "network",
                "price": 42000000,
                "duration_minutes": 0,
            },
        ],
    },
    {
        "code": "SUPP-003",
        "name": "CV Prima Konsultan Bisnis",
        "email": "billing@primakonsultan.id",
        "phone": "022-6655-8811",
        "country_code": "ID",
        "region_code": "32",
        "city_code": "32.73",
        "address": "Jl. Diponegoro No. 45, Bandung",
        "latitude": -6.9034,
        "longitude": 107.6187,
        "base_price": 0,
        "rating_avg": 4.7,
        "rating_count": 65,
        "notes": (
            "Professional consulting partner for accounting, "
            "audit, taxation, and ERP implementation."
        ),
        "products": [
            {
                "code": "CONSULT-001",
                "name": "Accounting Advisory Service",
                "category_code": "consulting",
                "price": 12000000,
                "duration_minutes": 0,
            },
            {
                "code": "AUDIT-001",
                "name": "Internal Audit Service",
                "category_code": "audit",
                "price": 25000000,
                "duration_minutes": 0,
            },
        ],
    },
    {
        "code": "SUPP-004",
        "name": "PT Artha Logistik Indonesia",
        "email": "accounting@arthalogistik.co.id",
        "phone": "031-7788-2221",
        "country_code": "ID",
        "region_code": "35",
        "city_code": "35.78",
        "address": "Jl. HR Muhammad No. 77, Surabaya",
        "latitude": -7.2575,
        "longitude": 112.7521,
        "base_price": 0,
        "rating_avg": 4.6,
        "rating_count": 73,
        "notes": (
            "Regional logistics and warehouse distribution partner "
            "for operational supply chain."
        ),
        "products": [
            {
                "code": "WAREHOUSE-001",
                "name": "Warehouse Distribution Service",
                "category_code": "logistics",
                "price": 18000000,
                "duration_minutes": 0,
            },
            {
                "code": "FREIGHT-001",
                "name": "Freight & Cargo Delivery",
                "category_code": "shipping",
                "price": 9500000,
                "duration_minutes": 0,
            },
        ],
    },
]
