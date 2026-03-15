# core/roles/enums.py

from enum import Enum


class RoleCode(str, Enum):

    GUEST = "guest"
    
    # Platform personas
    CUSTOMER = "customer"
    PARTNER = "partner"

    # Organization hierarchy
    VIEWER = "viewer"
    STAFF = "staff"
    SUPERVISOR = "supervisor"
    MANAGER = "manager"
    GM = "gm"
    DIRECTOR = "director"
    ADVISOR = "advisor"

    # Operations
    CASHIER = "cashier"
    WAREHOUSE = "warehouse"
    OPERATOR = "operator"
    TECHNICIAN = "technician"

    # Business functions
    FINANCE = "finance"

    # System
    ADMIN = "admin"
    OWNER = "owner"