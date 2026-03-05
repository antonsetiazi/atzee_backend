# verticals/marketplace/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — BUYER
    # ========================================
    {
        "tenant_code": None,
        "role": "Buyer",
        "type": "sidebar",
        "device": "desktop",
        "app": "marketplace",
        "items": [
            {"action_type": "page", "target": "marketplace.home", "icon": "home", "route": "/marketplace/home", "label": "Home"},
            {"action_type": "page", "target": "marketplace.browse", "icon": "search", "route": "/marketplace/browse", "label": "Browse"},
            {"action_type": "page", "target": "marketplace.categories", "icon": "grid", "route": "/marketplace/categories", "label": "Categories"},
            {"action_type": "page", "target": "marketplace.flash_sale", "icon": "zap", "route": "/marketplace/flash-sale", "label": "Flash Sale"},
            {"action_type": "page", "target": "marketplace.cart", "icon": "shopping-cart", "route": "/marketplace/cart", "label": "Cart"},
            {"action_type": "page", "target": "marketplace.orders", "icon": "package", "route": "/marketplace/orders", "label": "Orders"},
            {"action_type": "page", "target": "marketplace.wishlist", "icon": "heart", "route": "/marketplace/wishlist", "label": "Wishlist"},
            {"action_type": "page", "target": "marketplace.messages", "icon": "message-circle", "route": "/marketplace/messages", "label": "Messages"},
            {"action_type": "page", "target": "marketplace.notifications", "icon": "bell", "route": "/marketplace/notifications", "label": "Notifications"},
            {"action_type": "page", "target": "marketplace.account", "icon": "user", "route": "/marketplace/account", "label": "Account"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — SELLER
    # ========================================
    {
        "tenant_code": None,
        "role": "Seller",
        "type": "sidebar",
        "device": "desktop",
        "app": "marketplace",
        "items": [
            {"action_type": "page", "target": "marketplace.seller.dashboard", "icon": "home", "route": "/marketplace/seller/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "marketplace.products", "icon": "box", "route": "/marketplace/seller/products", "label": "Products"},
            {"action_type": "page", "target": "marketplace.orders", "icon": "package", "route": "/marketplace/seller/orders", "label": "Orders"},
            {"action_type": "page", "target": "marketplace.inventory", "icon": "archive", "route": "/marketplace/seller/inventory", "label": "Inventory"},
            {"action_type": "page", "target": "marketplace.shipping", "icon": "truck", "route": "/marketplace/seller/shipping", "label": "Shipping"},
            {"action_type": "page", "target": "marketplace.marketing", "icon": "megaphone", "route": "/marketplace/seller/marketing", "label": "Marketing"},
            {"action_type": "page", "target": "marketplace.finance", "icon": "credit-card", "route": "/marketplace/seller/finance", "label": "Finance"},
            {"action_type": "page", "target": "marketplace.reviews", "icon": "star", "route": "/marketplace/seller/reviews", "label": "Reviews"},
            {"action_type": "page", "target": "marketplace.customers", "icon": "users", "route": "/marketplace/seller/customers", "label": "Customers"},
            {"action_type": "page", "target": "marketplace.store", "icon": "store", "route": "/marketplace/seller/store", "label": "Store"},
            {"action_type": "page", "target": "marketplace.reports", "icon": "bar-chart", "route": "/marketplace/seller/reports", "label": "Reports"},
            {"action_type": "page", "target": "marketplace.settings", "icon": "settings", "route": "/marketplace/seller/settings", "label": "Settings"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — ADMIN
    # ========================================
    {
        "tenant_code": None,
        "role": "Admin",
        "type": "sidebar",
        "device": "desktop",
        "app": "marketplace",
        "items": [
            {"action_type": "page", "target": "marketplace.admin.dashboard", "icon": "home", "route": "/marketplace/admin/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "marketplace.users", "icon": "users", "route": "/marketplace/admin/users", "label": "Users"},
            {"action_type": "page", "target": "marketplace.stores", "icon": "store", "route": "/marketplace/admin/stores", "label": "Stores"},
            {"action_type": "page", "target": "marketplace.products", "icon": "box", "route": "/marketplace/admin/products", "label": "Products"},
            {"action_type": "page", "target": "marketplace.orders", "icon": "package", "route": "/marketplace/admin/orders", "label": "Orders"},
            {"action_type": "page", "target": "marketplace.payments", "icon": "credit-card", "route": "/marketplace/admin/payments", "label": "Payments"},
            {"action_type": "page", "target": "marketplace.shipping", "icon": "truck", "route": "/marketplace/admin/shipping", "label": "Shipping"},
            {"action_type": "page", "target": "marketplace.promotions", "icon": "megaphone", "route": "/marketplace/admin/promotions", "label": "Promotions"},
            {"action_type": "page", "target": "marketplace.reviews", "icon": "star", "route": "/marketplace/admin/reviews", "label": "Reviews"},
            {"action_type": "page", "target": "marketplace.disputes", "icon": "alert-circle", "route": "/marketplace/admin/disputes", "label": "Disputes"},
            {"action_type": "page", "target": "marketplace.reports", "icon": "bar-chart", "route": "/marketplace/admin/reports", "label": "Reports"},
            {"action_type": "page", "target": "marketplace.system", "icon": "settings", "route": "/marketplace/admin/system", "label": "System"},
        ],
    },

]