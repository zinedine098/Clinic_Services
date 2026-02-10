from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with role support."""

    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("loket", "Loket"),
        ("ugd", "UGD"),
        ("dokter", "Dokter"),
        ("farmasi", "Farmasi"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="loket")
    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def is_loket(self):
        return self.role == "loket"

    @property
    def is_ugd(self):
        return self.role == "ugd"

    @property
    def is_dokter(self):
        return self.role == "dokter"

    @property
    def is_farmasi(self):
        return self.role == "farmasi"
