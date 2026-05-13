# core/activity/constants/activity_types.py

"""
Universal activity target types.

Used for:
- timeline filtering
- websocket subscriptions
- automation rules
- AI grouping
- analytics
"""

# ============================================================
# FINANCE
# ============================================================

FIXED_ASSET = "fixed_asset"
INVOICE = "invoice"
PAYMENT = "payment"
JOURNAL_ENTRY = "journal_entry"
ACCOUNT = "account"

# ============================================================
# INVENTORY
# ============================================================

ITEM = "item"
WAREHOUSE = "warehouse"
STOCK_MOVEMENT = "stock_movement"
PURCHASE_ORDER = "purchase_order"

# ============================================================
# HRMS
# ============================================================

EMPLOYEE = "employee"
ATTENDANCE = "attendance"
PAYROLL = "payroll"
LEAVE_REQUEST = "leave_request"

# ============================================================
# SYSTEM
# ============================================================

USER = "user"
ROLE = "role"
TENANT = "tenant"
SETTING = "setting"

# ============================================================
# GENERIC HELPERS
# ============================================================

ALL_ACTIVITY_TYPES = [
    FIXED_ASSET,
    INVOICE,
    PAYMENT,
    JOURNAL_ENTRY,
    ACCOUNT,
    ITEM,
    WAREHOUSE,
    STOCK_MOVEMENT,
    PURCHASE_ORDER,
    EMPLOYEE,
    ATTENDANCE,
    PAYROLL,
    LEAVE_REQUEST,
    USER,
    ROLE,
    TENANT,
    SETTING,
]
