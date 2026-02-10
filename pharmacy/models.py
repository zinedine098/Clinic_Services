from django.db import models
from django.conf import settings
from examinations.models import Examination


class Medicine(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nama Obat")
    description = models.TextField(blank=True, verbose_name="Deskripsi")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stok")
    unit = models.CharField(max_length=30, default="tablet", verbose_name="Satuan")
    price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0, verbose_name="Harga"
    )
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "medicines"
        ordering = ["name"]
        verbose_name = "Obat"
        verbose_name_plural = "Obat"

    def __str__(self):
        return f"{self.name} (Stok: {self.stock})"


class Prescription(models.Model):
    examination = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE,
        related_name="prescriptions",
        verbose_name="Pemeriksaan",
    )
    medicine = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, verbose_name="Obat"
    )
    dosage = models.CharField(max_length=100, verbose_name="Dosis")
    quantity = models.PositiveIntegerField(verbose_name="Jumlah")
    instructions = models.TextField(blank=True, verbose_name="Aturan Pakai")
    is_dispensed = models.BooleanField(default=False, verbose_name="Sudah Diserahkan")
    dispensed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Diserahkan Oleh",
    )
    dispensed_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Waktu Penyerahan"
    )

    class Meta:
        db_table = "prescriptions"
        verbose_name = "Resep"
        verbose_name_plural = "Resep"

    def __str__(self):
        return f"{self.medicine.name} - {self.dosage} ({self.quantity})"
