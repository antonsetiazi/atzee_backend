# integrations/whatsapp/providers/fonnte.py

import requests
from django.conf import settings


FONNTE_URL = "https://api.fonnte.com/send"


def send_fonnte_message(phone: str, message: str):

    payload = {
        "target": phone,
        "message": message,
    }

    headers = {
        "Authorization": settings.FONNTE_API_KEY
    }

    response = requests.post(
        FONNTE_URL,
        data=payload,
        headers=headers
    )

    return response.json()