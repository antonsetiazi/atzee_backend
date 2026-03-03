# verticals/distributor/seeds/navigation.py

NAVIGATION_SEED = [

    # ======================================================
    # DESKTOP SIDEBAR — OWNER
    # ======================================================
    {
        "tenant_code": None,
        "role": "Owner",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "distributor.dashboard", "icon": "home", "route": "/distributor/dashboard", "label": "Executive Dashboard"},
            {"action_type": "page", "target": "distributor.sales_report", "icon": "bar-chart-2", "route": "/distributor/reports/sales", "label": "Sales Report"},
            {"action_type": "page", "target": "distributor.margin_report", "icon": "trending-up", "route": "/distributor/reports/margin", "label": "Margin Report"},
            {"action_type": "page", "target": "finance.aging", "icon": "alert-circle", "route": "/distributor/finance/aging", "label": "Receivable Aging"},
            {"action_type": "page", "target": "inventory.snapshot", "icon": "box", "route": "/distributor/inventory", "label": "Inventory Overview"},
            {"action_type": "page", "target": "distributor.settings", "icon": "settings", "route": "/distributor/settings", "label": "System Settings"},
        ],
    },

    # ======================================================
    # DESKTOP SIDEBAR — GENERAL MANAGER
    # ======================================================
    {
        "tenant_code": None,
        "role": "General Manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "distributor.dashboard", "icon": "home", "route": "/distributor/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "sales.orders", "icon": "shopping-cart", "route": "/distributor/sales/orders", "label": "Sales Orders"},
            {"action_type": "page", "target": "purchase.orders", "icon": "truck", "route": "/distributor/purchase/orders", "label": "Purchase Orders"},
            {"action_type": "page", "target": "inventory.snapshot", "icon": "box", "route": "/distributor/inventory", "label": "Inventory"},
            {"action_type": "page", "target": "finance.overview", "icon": "dollar-sign", "route": "/distributor/finance", "label": "Finance Overview"},
            {"action_type": "page", "target": "distributor.reports", "icon": "bar-chart", "route": "/distributor/reports", "label": "Reports"},
        ],
    },

    # ======================================================
    # DESKTOP SIDEBAR — SALES MANAGER
    # ======================================================
    {
        "tenant_code": None,
        "role": "Sales Manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "sales.dashboard", "icon": "activity", "route": "/distributor/sales/dashboard", "label": "Sales Dashboard"},
            {"action_type": "page", "target": "sales.orders", "icon": "shopping-cart", "route": "/distributor/sales/orders", "label": "Sales Orders"},
            {"action_type": "page", "target": "sales.delivery", "icon": "truck", "route": "/distributor/sales/delivery", "label": "Delivery Orders"},
            {"action_type": "page", "target": "sales.returns", "icon": "rotate-ccw", "route": "/distributor/sales/returns", "label": "Sales Return"},
            {"action_type": "page", "target": "sales.customers", "icon": "users", "route": "/distributor/sales/customers", "label": "Customers"},
            {"action_type": "page", "target": "sales.targets", "icon": "target", "route": "/distributor/sales/targets", "label": "Sales Target"},
        ],
    },

    # ======================================================
    # DESKTOP SIDEBAR — WAREHOUSE MANAGER
    # ======================================================
    {
        "tenant_code": None,
        "role": "Warehouse Manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "warehouse.dashboard", "icon": "home", "route": "/distributor/warehouse/dashboard", "label": "Warehouse Dashboard"},
            {"action_type": "page", "target": "inventory.snapshot", "icon": "box", "route": "/distributor/inventory", "label": "Stock Overview"},
            {"action_type": "page", "target": "warehouse.goods_receipt", "icon": "download", "route": "/distributor/warehouse/goods-receipt", "label": "Goods Receipt"},
            {"action_type": "page", "target": "warehouse.delivery", "icon": "truck", "route": "/distributor/warehouse/delivery", "label": "Delivery Orders"},
            {"action_type": "page", "target": "warehouse.adjustment", "icon": "shuffle", "route": "/distributor/warehouse/adjustment", "label": "Stock Adjustment"},
        ],
    },

    # ======================================================
    # DESKTOP SIDEBAR — FINANCE MANAGER
    # ======================================================
    {
        "tenant_code": None,
        "role": "Finance Manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "finance.dashboard", "icon": "activity", "route": "/distributor/finance/dashboard", "label": "Finance Dashboard"},
            {"action_type": "page", "target": "finance.invoices", "icon": "file-text", "route": "/distributor/finance/invoices", "label": "Invoices"},
            {"action_type": "page", "target": "finance.payments", "icon": "credit-card", "route": "/distributor/finance/payments", "label": "Payments"},
            {"action_type": "page", "target": "finance.aging", "icon": "alert-circle", "route": "/distributor/finance/aging", "label": "Receivable Aging"},
            {"action_type": "page", "target": "finance.ledger", "icon": "book", "route": "/distributor/finance/ledger", "label": "Ledger"},
        ],
    },

    # ======================================================
    # DESKTOP SIDEBAR — SALES REP (FIELD)
    # ======================================================
    {
        "tenant_code": None,
        "role": "Sales Rep",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "salesrep.dashboard", "icon": "home", "route": "/distributor/mobile/dashboard", "label": "My Dashboard"},
            {"action_type": "page", "target": "salesrep.orders", "icon": "shopping-cart", "route": "/distributor/mobile/orders", "label": "Create Order"},
            {"action_type": "page", "target": "salesrep.history", "icon": "clock", "route": "/distributor/mobile/history", "label": "Order History"},
            {"action_type": "page", "target": "salesrep.customers", "icon": "users", "route": "/distributor/mobile/customers", "label": "My Customers"},
        ],
    },

    # ======================================================
    # DESKTOP SIDEBAR — ADMIN SALES
    # ======================================================
    {
        "tenant_code": None,
        "role": "Admin Sales",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "sales.orders", "icon": "shopping-cart", "route": "/distributor/sales/orders", "label": "Sales Orders"},
            {"action_type": "page", "target": "sales.invoice_generate", "icon": "file-plus", "route": "/distributor/sales/invoice", "label": "Generate Invoice"},
            {"action_type": "page", "target": "sales.customers", "icon": "users", "route": "/distributor/sales/customers", "label": "Customers"},
        ],
    },

    # ======================================================
    # DESKTOP SIDEBAR — WAREHOUSE STAFF
    # ======================================================
    {
        "tenant_code": None,
        "role": "Warehouse Staff",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "warehouse.delivery", "icon": "truck", "route": "/distributor/warehouse/delivery", "label": "Delivery Orders"},
            {"action_type": "page", "target": "warehouse.goods_receipt", "icon": "download", "route": "/distributor/warehouse/goods-receipt", "label": "Goods Receipt"},
        ],
    },

    # ======================================================
    # DESKTOP SIDEBAR — FINANCE STAFF
    # ======================================================
    {
        "tenant_code": None,
        "role": "Finance Staff",
        "type": "sidebar",
        "device": "desktop",
        "app": "distributor",
        "items": [
            {"action_type": "page", "target": "finance.payments", "icon": "credit-card", "route": "/distributor/finance/payments", "label": "Payment Entry"},
            {"action_type": "page", "target": "finance.invoices", "icon": "file-text", "route": "/distributor/finance/invoices", "label": "Invoices"},
        ],
    },
]