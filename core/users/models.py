# core/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    avatar = models.ForeignKey(
        "core_files.File",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="user_avatars",
    )

    class Meta:
        db_table = "core_users"

    
    def __str__(self):
        return self.username


    @property
    def avatar_url(self):
        if not self.avatar:
            return None
        return self.avatar.get_download_url()