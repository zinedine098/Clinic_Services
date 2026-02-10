from django.db import models
from registrations.models import Registration
from doctors.models import Doctor


class Examination(models.Model):
    registration = models.OneToOneField(
        Registration,
        on_delete=models.CASCADE,
        related_name="examination",
        verbose_name="Registrasi",
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="examinations",
        verbose_name="Dokter",
    )
    diagnosis = models.TextField(verbose_name="Diagnosis")
    notes = models.TextField(blank=True, verbose_name="Catatan")
    treatment = models.TextField(blank=True, verbose_name="Tindakan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "examinations"
        ordering = ["-created_at"]
        verbose_name = "Pemeriksaan"
        verbose_name_plural = "Pemeriksaan"

    def __str__(self):
        return f"Exam #{self.id} - {self.registration.patient.name} by {self.doctor}"
