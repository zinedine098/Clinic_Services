from django.db import models


class Patient(models.Model):
    GENDER_CHOICES = [
        ("L", "Laki-laki"),
        ("P", "Perempuan"),
    ]
    medical_record_number = models.CharField(
        max_length=20, unique=True, verbose_name="No. Rekam Medis"
    )
    name = models.CharField(max_length=100, verbose_name="Nama Lengkap")
    birth_date = models.DateField(verbose_name="Tanggal Lahir")
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, verbose_name="Jenis Kelamin"
    )
    address = models.TextField(verbose_name="Alamat")
    phone = models.CharField(max_length=20, verbose_name="No. Telepon")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "patients"
        ordering = ["-created_at"]
        verbose_name = "Pasien"
        verbose_name_plural = "Pasien"

    def __str__(self):
        return f"{self.medical_record_number} - {self.name}"
