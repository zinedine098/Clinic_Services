from django.db import models
from django.conf import settings
from registrations.models import Registration
from polyclinics.models import Polyclinic


class Triage(models.Model):
    URGENCY_CHOICES = [
        ("low", "Rendah"),
        ("medium", "Sedang"),
        ("high", "Tinggi"),
        ("critical", "Kritis"),
    ]
    registration = models.OneToOneField(
        Registration,
        on_delete=models.CASCADE,
        related_name="triage",
        verbose_name="Registrasi",
    )
    complaint = models.TextField(verbose_name="Keluhan")
    blood_pressure = models.CharField(
        max_length=20, blank=True, verbose_name="Tekanan Darah"
    )
    temperature = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Suhu (°C)"
    )
    heart_rate = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Detak Jantung"
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Berat Badan (kg)",
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Tinggi Badan (cm)",
    )
    urgency_level = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default="low",
        verbose_name="Tingkat Urgensi",
    )
    referred_polyclinic = models.ForeignKey(
        Polyclinic, on_delete=models.CASCADE, verbose_name="Poli Tujuan"
    )
    assessed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Petugas",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "triages"
        ordering = ["-created_at"]
        verbose_name = "Triage"
        verbose_name_plural = "Triage"

    def __str__(self):
        return f"Triage #{self.id} - {self.registration.patient.name}"
