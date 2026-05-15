# verticals/finance/dashboard/constants/quick_actions.py

create_invoice = {
    "id": "create_invoice",
    "label": "Create Invoice",
    "icon": "receipt",
    "to": ("/finance/receivables/invoices/create"),
}

receive_payment = {
    "id": "receive_payment",
    "label": "Receive Payment",
    "icon": "wallet",
    "to": ("/finance/receivables/payments/create"),
}

customers = {
    "id": "customers",
    "label": "Customers",
    "icon": "users",
    "to": "/finance/customers",
}

add_asset = {
    "id": "add_asset",
    "label": "Add Asset",
    "icon": "building",
    "to": "/finance/assets/create",
}

reports = {
    "id": "reports",
    "label": "Reports",
    "icon": "chart",
    "to": "/finance/reports",
}
