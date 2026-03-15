# integrations/whatsapp/whatsapp_service.py

from .providers.fonnte import send_fonnte_message

class WhatsAppService:

    @staticmethod
    def send(phone: str, message: str):

        return send_fonnte_message(
            phone=phone,
            message=message
        )
    

'''
# ===================================================
# EXAMPLE
# =================================================== 
WhatsAppService.send(
    phone="6287827599638",
    message="Test WhatsApp dari Atzee 🚀"
)

Result:
{
    'detail': 'success! message in queue', 
    'id': [147150688], 
    'process': 'pending', 
    'quota': {
        '6287775586419': {
            'details': 'deduced from total quota', 
            'quota': 999, 
            'remaining': 998, 
            'used': 1
        }
    }, 
    'requestid': 416288263, 
    'status': True, 
    'target': ['6287827599638']
}
'''