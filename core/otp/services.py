# core/otp/services.py

"""
OTP Service

Central service responsible for generating, sending, and verifying
One-Time Passwords (OTP) used in authentication flows.

Security policies implemented here:

- OTP expiration: 5 minutes
- OTP attempt limit: 3 attempts
- OTP rate limit: 3 requests / 10 minutes
- OTP hashing: stored as SHA256

This service is designed to be provider-agnostic and currently
uses WhatsApp via Fonnte integration.

Used by:
- Auth login flow
- Phone verification
- Password reset
"""

from datetime import timedelta
from django.utils import timezone

from core.otp.utils.otp_generator import generate_otp
from core.otp.models import OTPCode
from core.otp.utils.hash import hash_otp
from integrations.whatsapp.whatsapp_service import WhatsAppService


"""
Architecture Note
-----------------

OTPService acts as a domain service for OTP operations.
Transport (WhatsApp, SMS, Email) should remain in integrations layer.

Core OTP logic must remain independent from external providers.
"""

class OTPService:

    @staticmethod
    def send_whatsapp_otp(phone: str) -> bool:
        """
        Generate and send OTP via WhatsApp.

        Security rules:
        - Max 3 OTP requests within 10 minutes.
        - OTP expires in 5 minutes.
        - OTP stored as SHA256 hash.
        """

        # Security: rate limit to prevent OTP spam
        recent_otp_count = OTPCode.objects.filter(
            phone=phone,
            created_at__gte=timezone.now() - timedelta(minutes=10)
        ).count()

        if recent_otp_count >= 3:
            raise Exception("Too many OTP requests. Please wait.")
        
        
        code = generate_otp()
        hashed_code = hash_otp(code)

        expired = timezone.now() + timedelta(minutes=5)

        OTPCode.objects.create(
            phone=phone,
            code=hashed_code,
            expired_at=expired
        )

        message = f"""
Kode OTP Anda: {code}

Jangan bagikan kode ini kepada siapapun.
Berlaku selama 5 menit.
"""

        WhatsAppService.send(phone, message)

        return True
    

    @staticmethod
    def verify_otp(phone: str, code: str):
        """
        Verify OTP for a phone number.

        Security rules:
        - OTP must not be expired.
        - Max 3 verification attempts.
        - OTP stored as SHA256 hash.

        Args:
            phone (str): Phone number.
            code (str): OTP provided by user.

        Returns:
            bool: True if OTP is valid.
        """
 
        try:
            otp = OTPCode.objects.filter(phone=phone).latest("created_at")
        except OTPCode.DoesNotExist:
            return False
 
        # Security: reject expired OTP
        if otp.expired_at < timezone.now():
            return False
        
        # Security: prevent brute-force attempts
        if otp.attempts >= otp.max_attempts:
            return False

        otp.attempts += 1
        otp.save(update_fields=["attempts"])

        # Security: compare hashed OTP
        if otp.code != hash_otp(code):
            return False

        return True