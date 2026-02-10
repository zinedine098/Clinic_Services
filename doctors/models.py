from django.db import models
from django.conf import settings
from polyclinics.models import Polyclinic


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
    )
    polyclinic = models.ForeignKey(
        Polyclinic,
        on_delete=models.CASCADE,
        related_name="doctors",
        verbose_name="Poliklinik",
    )
    specialization = models.CharField(
        max_length=100, blank=True, verbose_name="Spesialisasi"
    )
    license_number = models.CharField(max_length=50, blank=True, verbose_name="No. SIP")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "doctors"
        ordering = ["user__first_name"]
        verbose_name = "Dokter"
        verbose_name_plural = "Dokter"

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"
