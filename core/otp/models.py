# core/otp/models/otp_code.py

from django.db import models
from django.utils import timezone
import uuid


class OTPCode(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    phone = models.CharField(max_length=20)

    code = models.CharField(max_length=128)

    expired_at = models.DateTimeField()

    attempts = models.IntegerField(default=0)

    max_attempts = 3

    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.expired_at
    
    class Meta:
        db_table = "core_otp_code"
        ordering = ["-created_at"]
