# verticals/hr/dashboard/constants/quick_actions.py

create_invoice = {
    "id": "create_invoice",
    "label": "Create Invoice",
    "icon": "receipt",
    "to": ("/hr/receivables/invoices/create"),
}

receive_payment = {
    "id": "receive_payment",
    "label": "Receive Payment",
    "icon": "wallet",
    "to": ("/hr/receivables/payments/create"),
}

customers = {
    "id": "customers",
    "label": "Customers",
    "icon": "users",
    "to": "/hr/customers",
}

add_asset = {
    "id": "add_asset",
    "label": "Add Asset",
    "icon": "building",
    "to": "/hr/assets/create",
}

reports = {
    "id": "reports",
    "label": "Reports",
    "icon": "chart",
    "to": "/hr/reports",
}
