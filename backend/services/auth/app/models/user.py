from django.db import models
import uuid
from .login_type import LoginType
from django.contrib.auth.hashers import check_password
from asgiref.sync import sync_to_async


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    login_type = models.ForeignKey(
        LoginType, on_delete=models.CASCADE, null=False, blank=False
    )
    enable_2fa = models.BooleanField(default=False, null=False)
    password = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_active = models.BooleanField(default=False, null=False)
    is_first_login = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.user_name

    def check_password(self, password: str) -> bool:
        if password is None:
            return False
        return check_password(password, self.password)

    def to_safe_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "login_type": self.login_type.to_safe_dict(),
            "enable_2fa": self.enable_2fa,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_active": self.is_active,
            "is_first_login": self.is_first_login,
        }
