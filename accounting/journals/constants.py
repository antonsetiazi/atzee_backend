# accounting/journals/constants.py

class JournalType:
    GENERAL = "GENERAL"
    SALES = "SALES"
    PURCHASE = "PURCHASE"
    PAYMENT = "PAYMENT"
    PAYROLL = "PAYROLL"
    INVENTORY = "INVENTORY"
    ADJUSTMENT = "ADJUSTMENT"
    OPENING = "OPENING"
    CLOSING = "CLOSING"

    CHOICES = [
        (GENERAL, "General"),
        (SALES, "Sales"),
        (PURCHASE, "Purchase"),
        (PAYMENT, "Payment"),
        (PAYROLL, "Payroll"),
        (INVENTORY, "Inventory"),
        (ADJUSTMENT, "Adjustment"),
        (OPENING, "Opening Balance"),
        (CLOSING, "Closing"),
    ]


class JournalStatus:
    DRAFT = "DRAFT"
    POSTED = "POSTED"
    REVERSED = "REVERSED"

    CHOICES = [
        (DRAFT, "Draft"),
        (POSTED, "Posted"),
        (REVERSED, "Reversed"),
    ]