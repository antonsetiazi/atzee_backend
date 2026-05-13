# core/activity/constants/events.py

"""
Centralized universal activity event registry.

IMPORTANT:
- ALL event names should be defined here
- Avoid hardcoded event strings in modules
- Maintain consistent naming convention

Convention:
<domain>.<entity>.<action>

Examples:
finance.invoice.created
inventory.stock.adjusted
hrms.employee.promoted
system.user.login
"""

# ============================================================
# FINANCE
# ============================================================
FINANCE_FIXED_ASSET_CREATED = "finance.fixed_asset.created"
FINANCE_FIXED_ASSET_UPDATED = "finance.fixed_asset.updated"
FINANCE_FIXED_ASSET_DELETED = "finance.fixed_asset.deleted"
FINANCE_FIXED_ASSET_DEPRECIATED = "finance.fixed_asset.depreciated"
FINANCE_FIXED_ASSET_DEPRECIATION_RUN = "finance.fixed_asset.depreciation.run"
FINANCE_FIXED_ASSET_ACTIVATED = "finance.fixed_asset.activated"
FINANCE_FIXED_ASSET_DISPOSED = "finance.fixed_asset.disposed"
FINANCE_INVOICE_CREATED = "finance.invoice.created"
FINANCE_INVOICE_APPROVED = "finance.invoice.approved"
FINANCE_INVOICE_PAID = "finance.invoice.paid"
FINANCE_PAYMENT_CREATED = "finance.payment.created"

# ============================================================
# INVENTORY
# ============================================================
INVENTORY_ITEM_CREATED = "inventory.item.created"
INVENTORY_ITEM_UPDATED = "inventory.item.updated"
INVENTORY_STOCK_ADJUSTED = "inventory.stock.adjusted"
INVENTORY_PURCHASE_ORDER_CREATED = "inventory.purchase_order.created"
INVENTORY_PURCHASE_ORDER_APPROVED = "inventory.purchase_order.approved"

# ============================================================
# HRMS
# ============================================================
HRMS_EMPLOYEE_CREATED = "hrms.employee.created"
HRMS_EMPLOYEE_UPDATED = "hrms.employee.updated"
HRMS_EMPLOYEE_PROMOTED = "hrms.employee.promoted"
HRMS_PAYROLL_GENERATED = "hrms.payroll.generated"

# ============================================================
# SYSTEM
# ============================================================
SYSTEM_USER_LOGIN = "system.user.login"
SYSTEM_USER_LOGOUT = "system.user.logout"
SYSTEM_USER_CREATED = "system.user.created"
SYSTEM_ROLE_UPDATED = "system.role.updated"
SYSTEM_SETTING_UPDATED = "system.setting.updated"
