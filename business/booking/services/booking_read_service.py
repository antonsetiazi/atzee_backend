# business/booking/services/booking_read_service.py

def get_partner_name_from_order(order):
    if not order:
        return None

    items = list(order.items.all())
    if not items:
        return None

    listing = items[0].listing
    if not listing or not listing.partner:
        return None

    return str(listing.partner)