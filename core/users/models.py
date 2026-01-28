from django.contrib.auth.models import AbstractUser
from django.db import models
from core.tenants.models import Tenant


class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)


    class Meta:
        db_table = "core_users"

    
    def __str__(self):
        return self.username