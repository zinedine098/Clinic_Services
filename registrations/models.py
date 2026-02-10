from django.db import models
from patients.models import Patient


class Registration(models.Model):
    STATUS_CHOICES = [
        ("waiting_triage", "Menunggu Triage"),
        ("in_triage", "Sedang Triage"),
        ("waiting_exam", "Menunggu Pemeriksaan"),
        ("in_exam", "Sedang Diperiksa"),
        ("waiting_pharmacy", "Menunggu Farmasi"),
        ("completed", "Selesai"),
        ("cancelled", "Dibatalkan"),
    ]
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="registrations",
        verbose_name="Pasien",
    )
    queue_number = models.PositiveIntegerField(verbose_name="No. Antrian")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="waiting_triage",
        verbose_name="Status",
    )
    notes = models.TextField(blank=True, verbose_name="Catatan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "registrations"
        ordering = ["-created_at"]
        verbose_name = "Registrasi"
        verbose_name_plural = "Registrasi"

    def __str__(self):
        return f"REG-{self.id:05d} | {self.patient.name} | {self.get_status_display()}"

    @classmethod
    def get_next_queue_number(cls):
        from django.utils import timezone

        today = timezone.now().date()
        last = (
            cls.objects.filter(created_at__date=today).order_by("-queue_number").first()
        )
        return (last.queue_number + 1) if last else 1
