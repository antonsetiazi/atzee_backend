# shared/utils/phone.py

import re


def normalize_phone(phone: str) -> str:
    """
    Normalize phone number to Indonesian E.164 style without +.

    Examples:
        0812345678 -> 62812345678
        +62812345678 -> 62812345678
        62812345678 -> 62812345678
    """

    if not phone:
        raise ValueError("Phone number required")

    # remove spaces, dash, etc
    phone = re.sub(r"[^\d+]", "", phone)

    # remove +
    if phone.startswith("+"):
        phone = phone[1:]

    # convert 08 -> 628
    if phone.startswith("08"):
        phone = "628" + phone[2:]

    # convert 8xxxxx -> 628xxxxx
    if phone.startswith("8"):
        phone = "628" + phone

    if not phone.startswith("628"):
        raise ValueError("Invalid Indonesian phone number")

    return phone