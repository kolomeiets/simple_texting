from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username = None
    email = models.EmailField(
        "Email Address",
        unique=True,
    )
    phone_number = PhoneNumberField(blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email