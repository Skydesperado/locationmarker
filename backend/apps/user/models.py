from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, verbose_name="Username")
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_admin = models.BooleanField(default=False, verbose_name="Admin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
